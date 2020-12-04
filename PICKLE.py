import pickle

a = 1024

with open("duomenys.pkl", "wb") as failas:
   naujas_a =  pickle.dump(a,failas)                   #sukuria duomenys.pkl faila ir perduodam a elementa

with open("duomenys.pkl", "rb") as failas:   # perskaito faila
   naujas_a =  pickle.load(failas)

print(naujas_a)

# ZODYNAS

zodynas = {"vardas":"paulius","pavarde":"Rudinskas"}



