import psycopg2
from collections import defaultdict
from tts import GoogleTTS

class Tamara():

    """
        Handles data from the database


    """


    def __init__(self):
        print("init")

        self.tts = GoogleTTS()
        self.people = [0]
        self.people[0] = defaultdict(lambda: 'Vanilla')
        #defaultdict(self.people)
        #self.people = {}

        self.db = self.load_db()
        #self.sort_db(self.db)


    def main(self):
        print("Hello")


    def load_db(self, database="tamaradb"):
        """ loads database given param and returns list """

        db = []
        self.conn = psycopg2.connect(host="192.168.1.70", dbname=database, user='tamara')
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM public."overview"')
        self.db_vars = [x[0] for x in cur.description]

        db = cur.fetchall()
        self.conn.close()
        return db

    def sort_db(self, db):
        """
            Sorts db into a dictionary: Success but do I need to impletement?
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

    def save(self, user, table="public.overview", **kwargs):

        string = ""
        for key, val in kwargs.items():
            string+=f"{key}='{val}', "

        string = string[:-2]

        conn = psycopg2.connect(host="192.168.1.70", dbname="tamaradb", user='tamara')
        cur = conn.cursor()

        # log query as record
        query = f"UPDATE {table} SET {string} WHERE users='{user}'"
        print(query)
        cur.execute(query)
        conn.commit()
        cur.close()

    def find_index(self, column):
        index = [i for i,x in enumerate(self.db_vars) if x == column]
        return index[0]


    def say(phrase):
        self.tts.say(phrase)

    def play(filename):
        self.tts.play(filename)

if __name__ == "__main__":
    tam = Tamara()
