fname = input('ingrese nombre del archivo: ')
try:
    file = open(fname)
except:
    if fname == 'Holaaa' :
        print('OLEME LAS BOLAS')
        quit()
    else :
        print("ese archivo no existe (",fname,")")
        quit()
contador = 0
for linea in file :
    contador = contador +1
print('el archivo tiene ',contador,' lineas')
