import math

def hip(a,b):
    hipotenusa = math.sqrt((a**2) + (b**2))
    return hipotenusa

aCat = float(input('digite o valor do primeiro cateto: '))
bCat = float(input('digite o valor do segundo cateto: '))

print(hip(aCat, bCat))