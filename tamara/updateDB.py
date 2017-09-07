import psycopg2

def save(user, table="public.overview", **kwargs):

        string = ""
        for key, val in kwargs.items():
            string+=f"{key}={val}, "

        print(string)
        string = string[:-2]

        conn = psycopg2.connect(host="192.168.1.70", dbname="tamaradb", user='tamara', password='h12A98765')
        cur = conn.cursor()
        query = f"UPDATE {table} SET {string} WHERE users={user}"
        cur.execute(query)
        conn.commit()
        cur.close()

save(user="'master'", status=2015)
