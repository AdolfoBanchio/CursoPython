file = open('romeo.txt')
UniqW = list()
actual = list()
for line in file:
    actual = line.split()
    print(actual)
    for i in actual:
        print(i)
        if not i in UniqW:
            UniqW.append(i)

print('resultados')
print('palabras unicas')
UniqW.sort()
print(UniqW)
