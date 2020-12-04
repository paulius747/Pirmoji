
class Sakinys:
    def __init__(self,tekstas):           #inicijuoja
        self.tekstas = tekstas

    def atbulai(self):                   # Atbulai
        return self.tekstas[::-1]

    def mazosiomis(self):
        return self.tekstas.lower()    # mazosios

    def didziosiomis(self):
        return self.tekstas.upper()   #didziosios

    def grazinti_zodi(self, eilesnr):
        print(self.tekstas.split()[eilesnr])   # split grazina pasirinka zodi su ivestu index

    def simboliu_skaicius(self,simbolis):    # grazina simboliu skaiciu siuo atjevu "a" raide
        print(self.tekstas.count(simbolis))

    def pakeisti(self,pakeitimas,pakeitimas2):      # REPLACE METODAS
        print(self.tekstas.replace(pakeitimas,pakeitimas2))

    def zodis(self,skaicius):
        suskaidytas_string = self.tekstas.split()
        print(suskaidytas_string[skaicius])

    def info(self):
        zodziai = len(self.tekstas.split())
        skaiciu = sum(i.isnumeric() for i in self.tekstas)    #isnumeric() KEYWORD
        didziuju_raidziu = sum(i.isupper() for i in self.tekstas)       #isupper() KEYWORD
        mazuju_raidziu = sum(i.islower() for i in self.tekstas)     #islower() KEYWORD
        print(f"zodziai : {zodziai} skaiciai : {skaiciu} didziosios raides : {didziuju_raidziu} mazuju_raidziu : {mazuju_raidziu}")









sakinys1 = Sakinys("Labas rytas , Noriu Kavos")    # iniciuojam sakinys 1 Sakinys klaseje.

sakinys2 = Sakinys("Naujai Padeklarinas PVZ")

sakinys3 = Sakinys("UGUBUGU")

print(sakinys1.atbulai())

print(sakinys1.mazosiomis())

print(sakinys1.didziosiomis())

# DB BE PRINT TIESIO PER MOTODO ISKVIETIMA PRINT BUS DB METODE

sakinys1.grazinti_zodi(1)

sakinys1.simboliu_skaicius("a")

sakinys1.pakeisti("Labas","Krabas")

sakinys1.info()   # iskviestas sakinys1 info
sakinys2.info()  #  iskviestas sakinys2 info
sakinys3.info()  #  iskviestas sakinys3 info













