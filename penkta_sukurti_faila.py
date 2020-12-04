
with open("tekstas.txt", "w") as failas:  # sukuriame txt faila w raide reiskia write
    failas.write("Labas")   #faile parasome labas
    failas.seek(0)  #i kuri indexa nusokt
    failas.write("BE")
print("Programa baigta")

with open("tekstas.txt", "r") as failas:        # r reiskia read
    print(failas.read())           # read parodo kas faile yra

with open("tekstas.txt", "a", encoding="UTF-8") as failas: #  encoding="UTF-8"  leidzia importuo LT RAIDES
    failas.write(" AZUOLAS")                              # a raide append prideda pakeicia w write.

with open("tekstas.txt","r",encoding="UTF-8") as failas:
    print(failas.read())
    print(failas.readlines())
    