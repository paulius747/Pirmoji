
#Objekto klase
class Kate:
    def __init__(self,spalva,kojos):    # 1 Metodas default self - default ??????
        self.spalva = spalva
        self.kojos = kojos

    def miaukseti(self):       # 2 metodas default
        print("Miau")

    # def judinti_kojas(self):   #wtf
    #     pass
    #
    # def ziureti_kur_bega(self):  #wtf
    #     pass

    def begti(self):
        # self._judinti_kojas()
        # self._ziureti_kur_begi
        print("Begu")

    def miaukseta(self,zinute= "mUr" , kiekis= 1):  # jej nebus parametru naudos default parametrus
        print(zinute*kiekis)

    def __str__(self):
        return f"{self.spalva} kate su {self.kojos} kojomis"



#Objekto iniciavimas

kate1 = Kate("Balta",4)       # 2 kart iniciuojuojame

kate2 = Kate("Juoda",4)

print(kate1.spalva)        #ir 2 kart iskvies class kate ir 2x printins.
print(kate1.kojos)

print(kate2.spalva)      #ir 2 kart iskvies class kate ir 2x printins.
print(kate2.kojos)

kate2.spalva = "Pilka"   #paudatinam 2 kates spalva is juodos i pilka
print(kate2.spalva)

kate2.miaukseti()   #iskvieciam miaukseti metoda

kate1.begti()

kate1.miaukseta("Mur",4)     #Duodame parametrus

print(kate1)                # full kates objekto
print(kate2)

print(kate1.spalva)

pasisveikinimas = "sveikas pasauli"
labas = "Labas"

print(id(pasisveikinimas))   # ID duos
print(id(labas))       #ID duos










