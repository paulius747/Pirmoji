import sqlite3

duomenu_baze = sqlite3.connect("duomenu_baze2.db")
baze = duomenu_baze.cursor()

with duomenu_baze:                                      ## SUkuria duomenu baze ir uzdaro ?
    baze.execute("""CREATE TABLE IF NOT EXISTS
    Darbuotojai(
    Pavadinimas text,
    Destytoja text,
    Trukme integer
    )""")

with duomenu_baze:
    baze.execute("INSERT INTO darbuotojai VALUES('Vadyba','Domantas',40)")
    baze.execute("INSERT INTO darbuotojai VALUES('Python','Donatas',80)")
    baze.execute("INSERT INTO darbuotojai VALUES('Java','Tomas',80)")
    #   baze.execute("DELETE from Darbuotojai WHERE Destytoja = 'Tomas'")    #DELETE FUNKCIJA

    baze.execute("SELECT * From Darbuotojai WHERE trukme > 50")
    print(baze.fetchall())
    baze.execute("UPDATE darbuotojai SET pavadinimas ='Python programavimas' where pavadinimas = 'Python' ")
    baze.execute("DELETE from darbuotojai where destytoja = 'Tomas' ")
    baze.execute("SELECT * From darbuotojai")
    print(baze.fetchall())


