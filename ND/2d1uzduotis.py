
sarasas_skaicius = [10,20,30]

print(sarasas_skaicius[2])  # 2 array  index iskvieciamas
print(sarasas_skaicius)   #visa sarasa
sarasas_skaicius.append(40)   #prideda prie array
sarasas_skaicius.insert(3,50)   # 3 i kuria vieta pades , 50 idedamas skaicius
sarasas_skaicius.pop(2)   #trina pagal indexa
sarasas_skaicius.remove(50)       #trina kokia reiksme ivesi
sarasas_skaicius[0]= 15     #gerai ?   replace ?


print(sarasas_skaicius)


sarasas_zodynas = {"Paulius":27 , "Petras":20 , "Juozas": 25}

sarasas_zodynas["Jokubas"] = 52

del sarasas_zodynas["Paulius"]

sarasas_zodynas["Petras"] = "Pakeitimas"

print(sarasas_zodynas)




