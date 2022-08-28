def eficiencia(km, litro):
    consumo = km/litro

    if consumo < 8:
        print('Venda o carro!')
    elif consumo > 8 and consumo < 14:
        print('Econômico!')
    elif consumo > 12:   
        print('Super econômico!')

dist = float(input('digite a distancia em km: '))
cons = float(input('digite o consumo de gasolina em litros: '))

eficiencia(dist, cons)