import datetime

class Darbuotojas:

    def __init__(self,vardas,valandos_ikainis,dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.laikas_now = datetime.datetime.today()
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo,"%Y,%m,%d,%H,%M,%S")
        print(f"Dirba nuo : {self.dirba_nuo}")
        print(f"Dabartinis laikas : {self.laikas_now}")

    def _privatus_(self):
        self.nudirbo_dienu = self.laikas_now - self.dirba_nuo
        return self.nudirbo_dienu.days * 8


    def paskaiciuoti_atlyginima(self):
        atlyginimas = self.valandos_ikainis * self._privatus_()
        print(f"{self.vardas} uzdirbo {str(atlyginimas)}")

class NoramlusDarbuotojas(Darbuotojas):

    def _privatus_(self):
        self.nudirbo_dienu = self.laikas_now - self.dirba_nuo
        nudirbo_savaiciu = self.nudirbo_dienu / 7
        nudirbo_dienu_1 = self.nudirbo_dienu -(nudirbo_savaiciu*2)
        return nudirbo_dienu_1.days * 8


darbuotojas6 = Darbuotojas("Vasia",10,"2020,10,30,10,10,10")
darbuotojas6.paskaiciuoti_atlyginima()



darbuotojas1 =NoramlusDarbuotojas("Petras",10,"2020,10,30,10,10,10")
darbuotojas1.paskaiciuoti_atlyginima()





