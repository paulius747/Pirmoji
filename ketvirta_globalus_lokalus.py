

globalus = 10   # globalus variable

def funkcija():    #
    lokalus =12
    suma = globalus + lokalus
    print(suma)

def funkcija2():
    lokalus =12
    suma = globalus+ lokalus
    print(suma)
    return funkcija2()   # jeigu bus RETURN


kita_suma = globalus + lokalus    # meta errora nes lokalus uzdarytas funkcijose
kita_suma2 = globalus + funkcija2()     # VEIKS TIK TADA KAI FUNKCIJA TURES RETURN IR per funkcija kviesime

print(kita_suma)
print(kita_suma2)

#KOMENTARAI FUNKCIJOJE

def funkcija3(parametras1, parametras2):                    # TAIP IRASOME KOMENTARUS KURIE MATYSIS PAHOVERINUS VIRS FUNKCIJOS
    '''
    Ši funkcija visiškai nieko nedaro
    :param parametras1: Nereikalingas parametras
    :param parametras2: Dar vienas nereikalingas
    parametras
    :return: Nieko negražina
    '''
    return

funkcija3()            #pahoverinus matome komentarus kuriuos irasete