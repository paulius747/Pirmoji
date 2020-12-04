
class Automobilis:    # TEVINE KLASE

    def __init__(self,metai,modelis,kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f"Metai : {metai}  Modelis : {modelis}  Kuro tipai :{kuro_tipas}")
        print("--------------------------------------------------------------------")


    def vaziuoti(self):
        print("Vaziuoja VRUM VRUM")

    def stoveti(self):
        print("Parkanuli ant ruckos")

    def pildyti_degali(self):
        print("Degalai ipilti galima Vrum Vrum")


class Elektromobilis(Automobilis):

    def pildyti_degali(self):
        print("Batareike ant MAX galima VRUMx2")

    def vaziuoja_autonomiskai(self):
        print("HUMAN STUPID COMPUTER VROM VROM AUTONOMISKAI all hail overlord MUSK !")


masina1= Automobilis(2001 ,"BMW","Benzinas")

masina2= Automobilis(2020 , "Porche","Benzinas")

masina3_elektra = Elektromobilis(2020 ,"TESLA","Batareikos")


masina1.vaziuoti()
masina1.stoveti()
masina1.pildyti_degali()

print("--------------------------------------------------------")

masina3_elektra.vaziuoti()
masina3_elektra.stoveti()
masina3_elektra.pildyti_degali()
masina3_elektra.vaziuoja_autonomiskai()
