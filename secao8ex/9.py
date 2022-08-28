from math import pi
def volume(a, r):
    volume = pi * (r**2) * a
    return volume

altura = float(input('digite o valor da altura: '))
raio = float(input('digite o valor do raio: '))

print(f'o volume do cilindro é {volume(altura,raio)}')