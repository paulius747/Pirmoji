

sarasas = ["vienas ", 2 , True, 15 ,"dvidesimt"]

suma = 0

for x in sarasas:
    if type(x) is int or type(x) is float:
        suma +=x
    else:
        print("cia ne skaicius")

print("Skaiciu suma " , suma)