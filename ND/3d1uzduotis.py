program = True

while program:
    try:
        sveikas_skaicius = int(input("Iveskite sveika skaiciu"))

        ar_skaicius_teigiamas = sveikas_skaicius >= 0
        print("Ar skaicius teigiamas ?")

        if ar_skaicius_teigiamas:
            print(ar_skaicius_teigiamas)
            program = False
        else:
            print(ar_skaicius_teigiamas)
            program = False
    except ValueError:
        print("Blogas skaiciaus formatas , arba ivedete raide .....")
