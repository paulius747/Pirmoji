

try:                   #nurodo kur gali but klaida ?
    skaicius= int(input("iveskite skaicu"))            #ivesime string i bus error

except:
    print("Ivestas blogas skaicus")    # jeigu try nesuveiks suveiks except


print("Helllo words")          #sitas toliau vyksta net su erroru

try:
    skaicius= int(input("iveskite skaicu"))
except ValueError:                                #ideda mesage i console
    print("Ivestas blogas skaicus")
except ZeroDivisionError:
    print("dalyba is 0 negalima")
except FileNotFoundError:
    print("Nerado failo")
except:
    print("Ivyko klaida")
finally:
    print("failas uzdaromas")       # finally nusako kad ir kas vyks virsuje pabaigoje padaryk tai.


print("programa baigta")

if True:
    print("labas")
else:
    print("ate")

