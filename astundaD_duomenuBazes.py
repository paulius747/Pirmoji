import sqlite3

conn = sqlite3.connect("duomenu_baze.db")     ##SUkuria duomenu baze
c = conn.cursor()                               ##SUkuria duomenu baze

# with conn:                                      ## SUkuria duomenu baze ir uzdaro ?
#     c.execute("""CREATE TABLE IF NOT EXISTS
#     Darbuotojai(
#     Vardas text,
#     Pavarde text,
#     Atlyginimas integer
#     )""")

with conn:
    # c.execute("INSERT INTO darbuotojai VALUES('Paulius','Rudinskas', 350)")  #add/INSERT funkcija
    # c.execute("INSERT INTO darbuotojai VALUES('Jonas','Petraitis', 350)")  #ADD/INSERT FUNKCIJA
    # c.execute("DELETE from Darbuotojai WHERE Pavarde = 'Rudinskas'")    #DELETE FUNKCIJA
    # c.execute("UPDATE Darbuotojai SET Atlyginimas = 3000 WHERE Pavarde ='Rudinskas'")  # UPDATE FUNKCIJA
    c.execute("SELECT * From Darbuotojai ")
    print(c.fetchall())








