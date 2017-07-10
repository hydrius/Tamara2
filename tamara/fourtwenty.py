from tamara import Tamara
import datetime
import time

class BongOn():

    __SLEEP__ = 30

    def __init__(self):
        self.tamara = Tamara()

        # Why does this require [0]???
        self.users = self.tamara.load_db()[0]

    def main(self):

        while True:
            now = datetime.datetime.now()

            if now.hour == 16 and now.minute == 20:
                if(switch == 0):
                    self.tamara.say("Happy 420")
                    self.tamara.save(user="fourtwenty", table="public.modules", switch=1)

            if now.hour == 12 and now.minute == 5:
                    self.tamara.save(user="fourtwenty", table="public.modules", switch=0)

            time.sleep(__SLEEP__)

if __name__ == "__main__":
    bongon = BongOn()
    bongon.main()
