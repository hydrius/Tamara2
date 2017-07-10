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
    __PERIOD__ = 300

    def __init__(self):
        print("Am I home?")
        self.Tamara = Tamara()
        self.users = self.Tamara.load_db()[0] #returns list
        self.beginningoftime = datetime.datetime(2017, 1,1, 0, 0, 0)

    def main(self):
        """ Main function. Loops run forever """


        while True:
            # How fast is the call to the db?
            self.users = self.Tamara.load_db()
            print(self.users)
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


            now = datetime.datetime.now()

            # If online and previous status offline
            if mac in output.decode("utf-8") and status == 0:
                print("home ",user)
                print((now - finish).total_seconds())
                if (now - finish).total_seconds() > self.__PERIOD__:
                    print("action working")
                    self.action(self.users[i])
                self.Tamara.save(user=user, status=1, start=now,
                                 nsession=(nsession+1))

                #Update database
            elif mac in output.decode("utf-8"):
                print("still home ", user)
                self.Tamara.save(user=user, status=2, session=((now-start).total_seconds()/60))
                #update status in database to 2

            elif not mac in output.decode("utf-8") and status > 0:
                print("away", user)
                self.Tamara.save(user=user, status=0, finish=now)
    def action(self, user):
        print("ACTIONq  ")


if __name__ == "__main__":
    main = Home()
    main.main()
