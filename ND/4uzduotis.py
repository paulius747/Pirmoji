
skaicius1= int(input("Iveskite 1 skaiciu : "))

skaicius2= int(input("Iveskite 2 skaiciu : "))

veiksmas = input("Iveskite matematini veiksmas : + , - , / ,* .")


if veiksmas == "+":
    print(f"Sudetis {skaicius1+skaicius2}")
elif veiksmas == "-":
    print(f"Skirtumas {skaicius1 -skaicius2}")
elif veiksmas == "/":
    print(f"Dalyba  {skaicius1/skaicius2}")
elif veiksmas == "*":
    print(f"Daugyba {skaicius1*skaicius2}")