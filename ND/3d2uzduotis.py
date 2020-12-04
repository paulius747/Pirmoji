import datetime
from datetime import timedelta

laikas = datetime.datetime.now() #priskiriame laiko formata

print(laikas)   #original laikas

print(laikas - datetime.timedelta(days =5))   # atemame 5 dienas

print(laikas + datetime.timedelta(hours = 8))

print(laikas.strftime("%Y:%m:%d:%H:%M:%S"))