
class Gyvunas:                     # Tevine klase

    def __init__(self,vardas,spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print("Begu")


gyvunas1 = Gyvunas("tomas","juoda")

gyvunas2 = Gyvunas("peleda","Pilka")

gyvunas1.begti()

class Kate(Gyvunas):                            #iniciuojuoja classeje Kate claa Gyvunas ir jis perima visus parametrus ir def metodus
    pass

kate1 = Kate("Murka","ryza")
kate1.begti()

class Suo(Gyvunas):   # perduodam Suo gyvunas class ir metodus kol YRA PASS
    pass

suo1 = Suo("burzius","melynasis")
suo1.begti()

vezlys= Gyvunas("turtle","zalias")

vezlys.begti()


#OVER RIDE METODAS


class Vezlys(Gyvunas):
    def begti(self):   # PERASOME begti metoda ir jis overidina is Tevines klases.
        super().begti()
        print("begu letai")


gyvunas3 = Gyvunas("tomas","raudonas")
vezliagyvis = Vezlys("Piotr","Melynas")

gyvunas3.begti()
vezliagyvis.begti()