from tamara import Tamara
import datetime
import time

class BongOn():

    __SLEEP__ = 30


    def __init__(self):
        self.tamara = Tamara()

        # Why does this require [0]???
        self.modules = self.tamara.load_db(table='modules')
        self.modules = self.tamara.ret_row(self.modules, 'fourtwenty')
        print(self.modules)
        self.status = self.modules[self.tamara.find_index("status")]

    def main(self):

        while True:
            now = datetime.datetime.now()
            print(self.status)
            if now.hour == 16 and now.minute == 20:
                if(self.status == 0):
                    self.tamara.say("Happy 420")
                    self.tamara.save(user="fourtwenty", where="module", table="public.modules", status=1)

            if now.hour == 12:
                    self.tamara.save(user="fourtwenty", where="module", table="public.modules", switch=0)

            time.sleep(self.__SLEEP__)

if __name__ == "__main__":
    bongon = BongOn()
    bongon.main()
