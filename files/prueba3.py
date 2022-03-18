fname = input("ingrese el nombre del archivo: ")
try:
    file = open(fname)
except:
    print("ese archivo no existe (",fname,")")
    quit()
#cuento cuantos emitentes diferentes hubo
cuenta = 0
#creo las variables aux y aux2 para guardar la linea correspondiente al ultimo emisor y la ultima linea del archivo respectivamente
for line in file:
    aux2 = line.rstrip()
    if line.startswith('de:') and cuenta == 0 :
        aux = line.rstrip()
        print(aux)
        cuenta = cuenta +1
        print('primer if')
        continue
    if aux == aux2 :
        print('if del medio')
        continue
    elif line.startswith('de:') :
        cuenta = cuenta+1
        aux = line.rstrip()
        print('ultimo if')
print('hubo',cuenta,'emisores diferentes en tu inbox')
