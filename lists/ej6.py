largest = None
smallest = None
lista = list()
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
    	num = int(num)
    except:
        print('Invalid input')
        continue
    lista.append(num)

print("Maximum", max(lista))
print("Minimum", min(lista))
