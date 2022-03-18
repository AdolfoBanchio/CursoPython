fname = input('ingrese nombre del archivo: ')
try:
    file = open(fname)
except:
    print("ese archivo no existe (",fname,")")
    quit()
words = list()
contador = 0
for line in file :
    if line.startswith('From '):
        contador = contador + 1
        words = line.split()
        print(words[1])

print('hubo',contador,'lineas que comenzaron con "From "')
