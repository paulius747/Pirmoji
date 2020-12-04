# class Tevas:
#     def __init__(self, vardas ,pavarde):
#         self.vardas =vardas
#         self.pavarde = pavarde
#
#     def begti(self):
#         print("begu")
#
# class Vaikas(Tevas):                     # parasai class Vaikas(Tevas):  desniu klavisu generate overide metodes
#     def __init__(self, vardas, pavarde,mokykla):
#         super().__init__(vardas, pavarde)
#         self.mokykla = mokykla
#
#
# tevas1 = Tevas("rokas","budreika")
#
# vaikas = Vaikas("Urte","budrekaite","Barbora")
#
# print(tevas1.pavarde)

class Irasas:
    def __init__(self,suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    pass

class IslaiduIrasas(Irasas):
    pass

biudzetas =[]

irasas1 =PajamuIrasas(2000)

irasas2 = IslaiduIrasas(20)

biudzetas.append((irasas1))

biudzetas.append(irasas2)

for irasas in biudzetas:
    if isinstance(irasas,PajamuIrasas):
        print("pajamos: ",irasas.suma)
    if isinstance(irasas,IslaiduIrasas):
        print("islaidos : ",irasas.suma)


