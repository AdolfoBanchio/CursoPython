#creo lista de todos los emisores diferentes de mi imbox
fname = input("ingrese el nombre del archivo: ")
try:
    file = open(fname)
except:
    print("ese archivo no existe (",fname,")")
    quit()
#cuento cuantos emitentes diferentes hubo
cuenta = 0
emisores = list()
x = list()
#creo las variables aux y aux2 para guardar la linea correspondiente al ultimo emisor y la ultima linea del archivo respectivamente
for line in file:
    aux2 = line.rstrip()
    if line.startswith('de:') and cuenta == 0 :
        aux = line.rstrip()
        x = aux.split('<')
        emisores.append(x[1])
        cuenta = cuenta +1
        continue
    if aux == aux2 :
        continue
    elif line.startswith('de:') :
        cuenta = cuenta+1
        aux = line.rstrip()
        x = aux.split('<')
        emisores.append(x[1])
print('hubo',cuenta,'emisores diferentes en tu inbox')
print('lista de emisores: ')
print(emisores)
