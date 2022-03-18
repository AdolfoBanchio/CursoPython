file = open('inbox.txt')
#busco el emisor de el mail
'''
for x in file :
    x = x.rstrip()
    if x.startswith('de:'):
        print(x)}
'''
#alternativa
for x in file :
    x = x.rstrip()
    if not x.startswith('de:'):
        continue
    print(x)

print('se vuelve a repetir con la 2da alternativa')
#otra alternativa usando IN
file2 = open('inbox.txt')
for z in file2 :
    z = z.rstrip()
    if not 'de:'in z :
        continue
    print(z)
