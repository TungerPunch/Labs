import sqlite3;

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS classes(
   class TEXT NOT NULL,
   type TEXT NOT NULL,
   country TEXT NOT NULL,
   numGuns INT,
   bore REAL,
   displacement INT)""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS ships(
   name TEXT PRIMARY KEY NOT NULL,
   class TEXT NOT NULL REFERENCES classes(class),
   launched SMALLINT)""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS outcomes(
   ship TEXT PRIMATY KEY NOT NULL,
   battle TEXT NOT NULL,
   result TEXT NOT NULL)""")
conn.commit()
cur.execute(""" CREATE TABLE If NOT EXISTS battles(
    name varchar(20) PRIMARY KEY,
    [date] datetime 
)""")
conn.commit()
aclasses = [('Susano', '1', 'Konoha', 8, 15, 42000),
           ('Amaterasu', '2', 'Amegakure', 8, 15, 42000),
           ('Tsukuyomi', '3', 'Mizugakure', 8, 15, 42000)]
aships = [('a','Susano',2),
         ('b','Susano',2),
         ('c','Susano',2),
         ('d','Amaterasu',2),
         ('f','Amaterasu',2),
         ('e','Amaterasu',2),
         ('g','Tsukuyomi',2)]
aOutcomes = [('a','Fourth World War of Shinobi','sunk'),
            ('b','First World War of Shinobi','sunk'),
            ('c','First World War of Shinobi','ok'),
            ('d','Thirt World War of Shinobi', 'ok'),
            ('f','Second World War of Shinobi', 'ok'),
            ('e','Thirt World War of Shinobi', 'ok'),
            ('g','Second World War of Shinobi', 'sunk')]
aBattles = [
    ('First World War of Shinobi', '1641-03-24'),
    ('Second World War of Shinobi','1652-12-05'),
    ('Thirt World War of Shinobi','1958-07-12'),
    ('Fourth World War of Shinobi','1964-03-13')]
cur.executemany("INSERT INTO classes VALUES(?, ?, ?, ?, ?, ?);", aclasses)
cur.executemany("INSERT INTO ships VALUES(?, ?, ?);", aships)
cur.executemany("INSERT INTO Outcomes VALUES(?, ?, ?);", aOutcomes)
cur.executemany("INSERT INTO battles VALUES(?, ?);", aBattles)
conn.commit()
cur.execute("SELECT country FROM classes WHERE type='1' OR type='2'")
print(cur.fetchall())
