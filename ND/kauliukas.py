import random

while True:

    kauliukas1= random.randint(1,6)
    kauliukas2= random.randint(1,6)
    kauliukas3= random.randint(1,6)


    if kauliukas1 ==5 or kauliukas2 ==5 or kauliukas2 ==5:
        print("Pralaimejai")
        break                        #sustabdo jejgu pralaimejai
    else:
        print("Laimejai")