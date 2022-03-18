fname = input('ingrese nombre del archivo: ')
try:
    file = open(fname)
except:
    print("ese archivo no existe (",fname,")")
    quit()

spam = 0.0
contador = 0
for line in file :
    if line.startswith('X-DSPAM-Confidence:') :
        contador = contador+1
        strt = line.find(':')
        num = line[strt+1: ]
        num = num.strip()
        num = float(num)
        spam = spam + num
print('promedio spam confidence: ',spam/contador)
