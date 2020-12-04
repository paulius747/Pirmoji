total = 0

while True:

    skaicius = int(input("Iveskite skaiciu CIELA : "))
    if skaicius > 0:
        total += skaicius

    else:
        print("Total suma : " + str(total))
        print("ivestas minusinis skaicius")
        break
