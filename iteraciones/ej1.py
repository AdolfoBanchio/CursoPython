total = 0
cuenta = 0
while True :
    num = input('Ingrese un numero :')
    if num == 'done':
        break
    try:
        num = float(num)
        pass
    except:
        print("entrada invalida")
        continue
    cuenta = cuenta +1
    total = total + num

print(total, cuenta , total/cuenta)
