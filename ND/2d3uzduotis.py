zodziai = []

nariu_skaicius = int(input("iveskite vardu kieki : "))

for x in range(nariu_skaicius):
    ivestis = str(input("Iveskite zodi"))
    zodziai.append(ivestis)

print(zodziai)

for x in zodziai:
    print(x, "Ilgis : ", len(x), "Eiles numeris sarase : ", zodziai.index(x))
