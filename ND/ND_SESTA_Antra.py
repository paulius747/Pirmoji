import datetime
import calendar




class Sukaktis:
    def __init__(self,metai,menuo,diena,valanda,minute):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valanda = valanda
        self.minute = minute
        self.laikas = datetime.datetime(metai,menuo,diena, valanda,minute) #cia suformuluoja init metodo pilna data


    def smulkiai(self):
        laikas_now = datetime.datetime.now()    # TURIME SU LAIKU TAIP RASYT NES NERA NORM KLASIU
        skirtumas = laikas_now -self.laikas           # ir mum atiduoda tiktai days ir seconds formatu
        print("Praejo metu :" ,skirtumas.days//360)
        print("Praejo menesiu :" ,skirtumas.days/365*12)
        print("Praejo dienu : ",skirtumas.days)
        print("Praejo valandu :" ,skirtumas.seconds/3600)
        print("Praejo minuciu : ",skirtumas.seconds/60)
        print("Praejo sekundziu :" ,skirtumas.total_seconds())

    def ar_leap_year(self):                      # LEAP YEAR
        if calendar.isleap(self.metai):
            print("Keliamieji metai")

    def atimti_diena(self,dienos):                               #Dienu skirutmas
        print(self.laikas - datetime.timedelta(days=dienos))

    def pridetiDienas(self, dienos):
        print( self.laikas + datetime.timedelta(days=dienos))

    # def __str__(self):
    #     return (
    #         f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")

ivestis1 = int(input("Metai : "))
ivestis2 = int(input("Menesis : "))
ivestis3 = int(input("Diena :"))
ivestis4 = int(input("Valanda :"))
ivestis5 = int(input("Minutes : "))



ivesties_data = Sukaktis(ivestis1,ivestis2,ivestis3,ivestis4,ivestis5)
ivesties_data.smulkiai()
ivesties_data.ar_leap_year()
ivesties_data.atimti_diena(5)
ivesties_data.pridetiDienas(45)
print(ivesties_data)


