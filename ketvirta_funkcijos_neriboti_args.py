#  MASYVO TIPO
def daug_kvadratu(*args):    # *args leidzia ivesti neribota kieki args , kaip masyva padaro
    for skaicius in args:
        print(skaicius**2)
    print("-----------")




daug_kvadratu(5)    # 1 skaicius

daug_kvadratu(5,2,1,5,6,7,9,0)  # daug skaiciu

daug_kvadratu()   # empty siuo atveju grys tuscias


# DICTIONARY TIPO

def daug_kvadratu2(**kwargs):    # leidzia ivesti neribota kieki DICTIONARY tipo args
    for a , b in kwargs.items():
        print(a,b)
    print("-----------")


daug_kvadratu2(vardas= "paulius", pavarde = "rudinskas", amzius =100)  # turime ivedineti kaip dictionary tipo args name = value

