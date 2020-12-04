
sarasas = [45,25,34,56]



def funkcija(a):
    return a**2

sarasas2 = list(map(lambda a: a ** 2,sarasas))   #pritaikome lambda funkcija

kvadratu = lambda a: a ** 2

print(funkcija(5))   # kvieciam kaip normalia funkcija

print(kvadratu)   # kvieciame kvadratu var  kuriame yra lambda funkcija


