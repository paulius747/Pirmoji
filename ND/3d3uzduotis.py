import datetime
from datetime import timedelta
program =True
while program:
    try:

        iveskite_metus = str(input("Iveskite gimimo data ir laika YYYY-mm-dd-HH-MM-ss formatu"))
        dabartinis_laikas = datetime.datetime.now()
        metai = datetime.datetime.strptime(iveskite_metus, "%Y-%m-%d-%H-%M-%S")

        laiko_skirtumas = dabartinis_laikas - metai

        print(laiko_skirtumas)

        print("Praejo metu : ", round(laiko_skirtumas.days / 365))
        print("Praejo menesiu : ", round(laiko_skirtumas.days / 365 * 12))
        print("Praejo dienu : ", laiko_skirtumas.days)
        print("Praejo valandu : ", round(laiko_skirtumas.total_seconds() / 3600))
        print("Praejo minuciu : ", round(laiko_skirtumas.total_seconds() / 60))
        print("Praejo sekundziu : ", round(laiko_skirtumas.total_seconds()))
        program = False
    except ValueError:

         print("Blogas ivedimas arba formatas 3xLOL UltraN00b")





