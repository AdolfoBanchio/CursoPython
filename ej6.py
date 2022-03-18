h = input('Ingrese las horas que trabaja : ')
r = input('Ingrese paga por hora : ')
try:
    h = float(h)
    r = float(r)
except:
    print("ERROR,debe introducir numeos")
    quit();
def computepay(horas , rate):
    if horas > 40:
        print("Horas extra")
        paga = 40 * rate
        horas = horas - 40
        paga = paga + (horas*(1.5*rate))
    else:
        print("Regular")
        paga = horas * rate
    return(paga)

sueldo = computepay(h,r)

print('el sueldo es : ', sueldo)
