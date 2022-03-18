fname = input('ingrese nombre del archivo: ')
try:
    file = open(fname)
except:
    print("ese archivo no existe (",fname,")")
    quit()
for linea in file :
    print(linea.upper())
