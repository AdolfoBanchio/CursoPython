#extraigo el numero del final de la oracion
text = "X-DSPAM-Confidence:    0.8475"
strt = text.find(':')
num = text[strt+1: ]
print(num)
num = num.strip()
print(num)
num = float(num)
print(num)
