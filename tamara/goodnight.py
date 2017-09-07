from tamara import Tamara
import datetime

class GoodMorningAndGoodNight():

    def __init__(self):
        self.Tamara = Tamara()
        self.status = 1

    def main(self):
        while True:
            now = datetime.datetime.now()
            if status == 1:
                if now.hour == 21 and now.minute == 0:
                    self.Tamara.say("Good. night. sluts", override=True)
                    status = 0
                elif now.hour == 9 and now.minute == 0:
                    self.Tamara.say("Good. Morning. Coffee?", override=True)
                    status = 0
            if now.hour == 12 or now.hour == 7:
                status = 1

if __name__ == "__main__":
    x = GoodMorningAndGoodNight()
    x.main()
