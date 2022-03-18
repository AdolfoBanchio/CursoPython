def chop (t):
    del t[0]
    del t[(len(t)-1)]

print('Ingrese una lista')
lista = list()
listastr = input()
listastr = listastr[1:len(listastr)-1]
print(listastr)
lista = listastr.split(',')
listaDOS = listastr.split(',')

print(lista)
x = chop(lista)

print(lista)
print(x)

def middle(z):
    return z[1:len(z)-1]

y = middle(listaDOS)

print(listaDOS)
print(y)
