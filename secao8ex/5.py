from math import pi
def volume(r):
    return (4/3) * pi * (r ** 3)

raioCalc = float(input('digite o valor do raio: '))
print(f'o valor do volume é {volume(raioCalc)}')