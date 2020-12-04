
sarasas = [0,2,4,6,8,20]

ieskomasis = int(input("Iveskite ieskoma skaiciu"))


for x in sarasas:
    print(x)
    if x== ieskomasis:
        print("skaicius rastas")
        break
else:
    print("Skaicius nerastas")

print("programos pabaiga")



