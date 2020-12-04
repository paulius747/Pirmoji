
#year_input = int(input("Iveskite metus"))

year_input = 1900

while year_input<=2100:


    if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 ==0):
        print(year_input," keliamieji metai")
    #else:
       # print(year_input, " nekeliamieji metai")
    year_input += 1