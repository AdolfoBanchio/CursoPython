horas = input('Ingrese las horas que trabaja : ')
rate = input('Ingrese paga por hora : ')
horas = float(horas)
rate = float(rate)
if horas > 40:
    print("Horas extra")
    paga = 40 * rate
    horas = horas - 40
    paga = paga + (horas*(1.5*rate))
else:
    print("Regular")
    paga = horas * rate

print('el sueldo es : ',paga)
