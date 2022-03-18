file = open('prueba.txt')
cuenta = 0
todo = file.read()
print(len(todo))
print('archivo hasta la linea el 3 caracter \n ', todo[:3] )
print('archivo completo')
file = open('prueba.txt')
for a in file:
    cuenta = cuenta +1
    print(a)

print('cantidad de lineas', cuenta)
