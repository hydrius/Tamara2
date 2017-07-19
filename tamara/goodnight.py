from tamara import Tamara
import datetime

class GoodMorningAndGoodNight():

    def __init__(self):
        self.Tamara = Tamara()

    def main(self):
        while True:
            now = datetime.datetime.now()
            if now.hour == 21 and now.minute == 0:
                self.Tamara.say("Good. night. sluts", override=True)
            elif now.hour == 9 and now.minute == 0:
                self.Tamara.say("Good. Morning. Coffee?", override=True)

if __name__ == "__main__":
    x = GoodMorningAndGoodNight()
    x.main()
