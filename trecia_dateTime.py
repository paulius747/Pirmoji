import datetime   # import laiko paketa


print(datetime.datetime.now()) #data ir laikas

print(datetime.date.today())  #data


manodata = datetime.datetime(2020 ,2,29,18,20,50)   # eiliskumas : metai men diena val min s


manodata2 = datetime.date(2020 ,2,29)   #eiliskumas metai men diena

print(manodata)

print(manodata2)

print(manodata.strftime("%A"))       # laiko formato keitimas

laikas = datetime.datetime.today()      #today laikas

print(laikas + datetime.timedelta( days =5 , hours =5))   # matematika su laiku pridet atimt

kovo11 = datetime.datetime(1990,3,11)    #paskelbiame nauja data

skirtumas_laiko = laikas -kovo11

print(skirtumas_laiko.days)    # dienu skirtumas

print(skirtumas_laiko.seconds)   # sekundziu skirtumas

print("Kovo 11 : " ,kovo11.day)     #kovo 11 diena
print(kovo11.month)    #kovo 11 month
print(kovo11.year)    #kovo 11 year

# LAIKO IVEDIMAS USER !!!!!!!!!!!!!!!!!!!!

iveskite_data = input("Iveskite data : ")     # ivedame string data

data = datetime.datetime.strptime(iveskite_data,"%Y-%m-%d")   # is string padaro data normalia , bet reik ivest datos formatus .

print("Pagaminta data",data)

skirtumas3 = datetime.datetime.today() - data   #skirtumas

print(skirtumas3.days)