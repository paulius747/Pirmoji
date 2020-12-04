

def skaiciu_suma(skaicius1,skaicius2,skaicius3):     #funkcijos su daugiau argumentu
    suma = skaicius1 + skaicius2                       #returnina tik 1 variable daugiau negasli ?
    daugyba = suma * skaicius3
    return daugyba



print(skaiciu_suma(45,78,2))

def skaiciu_suma2(skaicius1,skaicius2,skaicius3=1):       # ivedame 1 variable jau preset/default ir td iskvieciant
    suma = skaicius1 + skaicius2
    daugyba = suma * skaicius3
    return daugyba

print(skaiciu_suma2(45, 78,30))              # ir iskvieciant ivedame tik 2 parametrus nes 3 jau preset
                                  #BET JEIGU IVESIME TRECIA VAR JIS IGNORUOS preset

#  print(skaiciu_suma2(45, 78,input()))      # galima naudoti ir INPUT

 #  skaiciu_suma(10)     ivedam 1 arg
  # skaiciu_suma(10,10)   ivedam 2 arg
   #skaiciu_suma(10,10,10)  ivedas 3 arg

# skaiciu_suma(skaicius3 = 100)     ivedam 1 arg   su pavadinimu