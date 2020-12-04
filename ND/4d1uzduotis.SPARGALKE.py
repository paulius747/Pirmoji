#1
def paduoti_skaiciai(a,b,c):     # paprasta suma funkcijoje
    suma = a+b+c
    return suma

print(paduoti_skaiciai(5,4,5))

#2


sarasas = [10 ,20 ,30,40]


def saraso_suma(masyvas):          # array listo suma  funkcija
    suma = 0
    for numbers in masyvas:
        suma +=numbers
    return suma
print(saraso_suma(sarasas))
#3

sarasas2 = [100 ,20 ,30,40]              #didziausias arrays elementas

def didziausias(*args):
    for numbers in args:
        return max(args)

print(didziausias(sarasas2))


#4

stringas = "Stringas atbulai"      # ATBULAI STRING

def atbulai(stringas):
    print(stringas[::-1])

atbulai(stringas)

#5

stringas2 = "Stringas atbulai Stringas atbulai Stringas atbulai222"

def stringas_kiek_zodziu(variable):
    kiek = variable.split()
    print(f"Zodziu kiekis : ",{len(kiek)})
    print(f"Capital raidziu kiekis : ",{len([char for char in stringas2 if char.isupper()])})  # suskaiciuoja didziasias radides
    print(f"Mazuju raidziu skaicius :",{len([char for char in stringas2 if char.islower()])})  # suskaiciuoja mazasias raides
    print(f"Skaiciu kiekis  :",{len([char for char in stringas2 if char.isnumeric()])})   #skaicius

stringas_kiek_zodziu(stringas2)


#6               # graziname sarasa pateikdami UNIKALIUS SARASO ELEMENTUS

unikaslus_sarasas = [20 , 40 , "Paulius ",18 ,50]

def print_selected(*args):
    for x in args:
        print(unikaslus_sarasas[x])


print_selected(0,2)

#7              # PASITIKRINK AR UZTENKA EXEPTIONS 
program = True
while program:

 skaicius =int(input("Iveskite pirmini skaiciu"))

 def pirminis(x):
         if x <= 1 or x % 2 ==0 or x % 3 ==0 or x % 5 == 0:
            print("Nepirminis skaicius")
         elif x == 2 or 3 or 5 or 7:
            print("Pirminis skaicius")
         else:
            print("Pirminis skaicius")


 pirminis(skaicius)


 











