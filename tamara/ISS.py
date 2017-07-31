import datetime
import time
import requests
import json
from tamara import Tamara

class SpaceStationNotifier():

    __SLEEP__ = 5

    def __init__(self):
        self.hasRun = False
        self.dailyReload = False
        self.Tamara.__logger__("SpaceStationNotifier is online")

    def run(self):
        while True:
            now = datetime.datetime.now().time()
            now_epoch = time.time()
            if self.dailyReload == False:
                r = requests.get('http://api.open-notify.org/iss-pass.json?lat=-32&lon=116')
                self.data = json.loads(r.text)
                self.dailyReload = True

            if now.hour == 12 and now.minute == 00:
                self.dailyReload = False

            # Because you can't see the space station during the day. DUH!
            if now.hour > 16:

                for flight in self.data["response"]:
                    flyover_epoch = flight["risetime"]

                    # All epoch times are GMT
                    #print("-------------------------")
                    #print(flyover_epoch)
                    #print(now_epoch)
                    #print("equals")
                    #print(flyover_epoch - now_epoch)
                    #print("--------------------------")
                    #print("--------------------------")

                    if flyover_epoch - now_epoch < 600:
                        if self.prev != flyover_epoch:
                            self.hasRun = False
                            self.prev = flyover_epoch

                    if flyover_epoch - now_epoch < 600 and flyover_epoch - now_epoch > 555:
                        self.Tamara.say("Ten minutes until space station visible")
                        self.prev = flyover_epoch
                        self.hasRun = True

                    if flyover_epoch - now_epoch < 10 and flyover_epoch - now_epoch > 0 and self.hasRun == True:
                        seconds = int(flyover_epoch - now_epoch)
                        self.Tamara.say(f"{seconds} until international space station flies over")
