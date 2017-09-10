import psycopg2
from collections import defaultdict
from tts import GoogleTTS
import datetime

class Tamara():

    """
        Handles data from the db.
    """

    def __init__(self):

        self.tts = GoogleTTS()

        # Why did I do this again? Why a vanilla dictionary?

        self.people = [0]
        self.people[0] = defaultdict(lambda: 'Vanilla')
        #defaultdict(self.people)
        #self.people = {}

        self.__logger__("Loading database")
        self.db = self.load_db()
        #self.sort_db(self.db)

    def __logger__(self, log, verbose=1):

        if verbose == 1:
            print(log)
        elif verbose <= 2:
            print(log)
        elif verbose <= 3:
            print(log)


    def main(self):
        print("Hello")

    def load_db(self, table='public.overview', database="tamaradb"):
        """ loads database given param and returns list
            - table='overview'
            - database='tamaradb'
        """

        db = []
        try:
            self.conn = psycopg2.connect(host="192.168.1.70", dbname=database, user='tamara')
            cur = self.conn.cursor()
            cur.execute(f"SELECT * FROM {table}")
            self.db_vars = [x[0] for x in cur.description]

            db = cur.fetchall()
            self.conn.close()

        except Exception as e:
            self.__logger__(e)
            pass

        return db

    def sort_db(self, db):
        """
            Sorts db into a dictionary: Success but does not need to be implement?
        """

        #self.db_vars = ["Name", "MAC", "status", "last"]
        for i, line in enumerate(db):
            for y, varz in enumerate(self.db_vars):
                try:
                    self.people[0][varz] = line[y]
                except IndexError:
                    self.people[0][varz] = None

        print(self.people[0].keys())
#                if line[i] is not None:
#                    self.people[line[0]][db_vars[i]]

    def save(self, user, where="users", table="public.overview", **kwargs):

        string = ""
        for key, val in kwargs.items():
            string+=f"{key}='{val}', "

        string = string[:-2]
        try:
            conn = psycopg2.connect(host="192.168.1.70", dbname="tamaradb", user='tamara')
            cur = conn.cursor()

            # log query as record
            query = f"UPDATE {table} SET {string} WHERE {where}='{user}'"
            self.__logger__(query)
            cur.execute(query)
            conn.commit()
            cur.close()
        except:
            pass

    def find_index(self, column):
        index = [i for i,x in enumerate(self.db_vars) if x == column]
        #self.__logger__(f"{column} is located on index: {index}")
        return index[0]

    def ret_row(self, list1, name):
        """ What does this do """
        self.__logger__(f"{list1} and {name}")
        for i, item in enumerate(list1):
            if name in item:
                return item

    def say(self, phrase, override=False):
        now = datetime.datetime.now()
        if (now.hour > 8 and now.hour < 21) or override==True:
            self.tts.say(phrase, "en")


    def play(self, filename):
        self.tts.play(filename)


    def online(self):
        """
        queries database and returns all who is online
        """
        query = 'SELECT * FROM public.overview where status>0'
        conn = psycopg2.connect(host="192.168.1.70", dbname="tamaradb", user='tamara')
        cur = conn.cursor()
        cur.execute(query)
        row = cur.rowcount
        return row

if __name__ == "__main__":
    tam = Tamara()
