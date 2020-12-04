
def funkcijos_name():                          #paskelbiame funkcija
    print("sveikas pasauli")


funkcijos_name()

def pasisveikink(vardas):     #funkcija su parametru , argumentu   su string
    print("labas",vardas)


pasisveikink("Paulius")
pasisveikink("petreas")


def kvadratas(skaicius):           #funkcija su parametru , argumentu   su skaiciais
    kvadratu = skaicius **2
    print(kvadratu)
    return kvadratu          #grazina kvadraTU

kvadratas(3)
kvadratas(9)

print(5+kvadratas(3))         # GRAZINIA I SITA VIETA kvadratu

