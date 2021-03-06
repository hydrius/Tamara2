#!/usr/bin/python

from tamara import Tamara # Use Module

import datetime
import os
import subprocess
import sys
import time


class Home():

    """ This class detects who has connected to the wifi.
        It has no params.

        The only data it uses include
        - User
        - Mac
        - Status
        - Filename (File)
        - Saying

        It has write properties to the db
        - Status
    """

    __SLEEP__ = 5
    __PERIOD__ = 600

    def __init__(self):

        self.Tamara = Tamara()
        self.Tamara.__logger__("Am I Home?")
        self.users = self.Tamara.load_db() #returns list
        self.beginningoftime = datetime.datetime(2017, 1,1, 0, 0, 0)

    def main(self):
        """ Main function. Loops run forever """
        while True:
            # How fast is the call to the db?
            self.users = self.Tamara.load_db()
            #print(self.users)
            # How long does this function take?
            self.run()
            time.sleep(self.__SLEEP__)


#    #def find_index(self, column):
#        index = [i for i,x in enumerate(self.Tamara.db_vars) if x == column]
#        print(index[0])
#        return index[0]

    def run(self):
        """ Search for users and commits actions
            # TO DO.
            - Put in own thread??
        """
        p = subprocess.Popen("arp-scan -l", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()

        for i,users in enumerate(self.users):

            user = users[self.Tamara.find_index("users")]
            mac = users[self.Tamara.find_index("mac")].lower()
            status = int(users[self.Tamara.find_index("status")])

            finish = users[self.Tamara.find_index("finish")]
            start = users[self.Tamara.find_index("start")]
            session = users[self.Tamara.find_index("session")]
            nsession = users[self.Tamara.find_index("nsession")]

            speech = users[self.Tamara.find_index("EntrySpeech")]
            media = users[self.Tamara.find_index("media")]

            now = datetime.datetime.now()

            # If online and previous status offline
            if mac in output.decode("utf-8") and status == 0:
                secondsOffline = (now - finish).total_seconds()
                self.Tamara.__logger__(f"home {user}: Offline total seconds: {secondsOffline}")

                if (now - finish).total_seconds() > self.__PERIOD__:
                    self.action(self.users[i], media, speech)

                    nsession += 1
                self.Tamara.save(user=user, status=1, start=now,
                                 nsession=(nsession))

            #Update database
            elif mac in output.decode("utf-8"):
                self.Tamara.save(user=user, status=2, session=((now-start).total_seconds()))
                #update status in database to 2

            elif not mac in output.decode("utf-8") and status > 0:
                self.Tamara.save(user=user, status=0, finish=now)


    def action(self, user, media, speech):
        self.Tamara.__logger__(f"{user}, {media}, {speech}")
        time.sleep(30)
        if media is not None:
            self.Tamara.play(media)
            print(media)
        else:
            print(media)

        if speech is not None:
            self.Tamara.say(speech)
            print(speech)
        else:
            print(speech)


if __name__ == "__main__":
    main = Home()
    main.main()
