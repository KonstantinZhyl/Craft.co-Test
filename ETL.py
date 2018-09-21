import sqlite3
import csv
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        conn.close()


create_connection(r"C:\sqlite\db\jobs.db")
conn = sqlite3.connect("C:\sqlite\db\jobs.db")
mycursor = conn.cursor()

# mycursor.execute("""DROP TABLE locations""")
# mycursor.execute("""DROP TABLE types""")
# mycursor.execute("""DROP TABLE jobs""")
# conn.commit()

mycursor.execute("""CREATE TABLE locations (id INTEGER PRIMARY KEY, name VARCHAR(255))""")
mycursor.execute("""CREATE TABLE types (id INTEGER PRIMARY KEY, type varchar(255))""")
mycursor.execute("""CREATE TABLE jobs (vacancy VARCHAR(255),
                                        team VARCHAR(255),
                                        employmentId INTEGER,
                                        locationId INTEGER,
                                        FOREIGN KEY (employmentId) REFERENCES types (id),
                                        FOREIGN KEY (locationId) REFERENCES location (id))""")

val = []
with open(sys.argv[-1], 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if row:
            val.append(row)
val = val[1:]

types = list({x[2] for x in val})
sql = """INSERT INTO types VALUES (?, ?)"""
mycursor.executemany(sql, [[i, types[i]] for i in range(len(types))])

locations = list({x[3] for x in val})
sql = """INSERT INTO locations VALUES (?, ?)"""
mycursor.executemany(sql, [[i, locations[i]] for i in range(len(locations))])

for value in val:
    value[2] = types.index(value[2])
    value[3] = locations.index(value[3])

sql = """INSERT INTO jobs VALUES (?, ?, ?, ?)"""
mycursor.executemany(sql, val)

conn.commit()
conn.close()
print("Done")
