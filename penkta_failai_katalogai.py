
import os   # importinam

# print(os.getcwd())   # kur yra work directory

os.chdir('C:\\Users\\User\\Desktop\\naujas katalogas')      # nurodom kur vyks veiksmas

print(os.listdir())

print(os.stat("kovos klubas.jpg").st_size)

# os.mkdir("naujas katalogas")    # sukuria kataloga desktop

# os.makedirs("Naujaskatalogas2/viduje/dar vienas")    # sukuria foledi / jame folderi / jame folderi