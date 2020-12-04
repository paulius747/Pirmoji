

sarasas = [12,52,85,89,77]

suma =0

for x in sarasas:         # ciklas sudarantis suma saraso elementu
    suma+=x

for skaicius in sarasas:     # ispaudsdina visus saraso elemento po 1
    print(skaicius)

print(suma)      #suma visu elementu

sarasas_kvadratu = []    #sukuriam array

for x in sarasas:                       #i sukurta sarasa is seno saraso imame  elementus ir su for ciklu ir append funkcija keliame kvadratu.
    sarasas_kvadratu.append(x**2)

print(sarasas_kvadratu)