lista = []
positivos = []
negativos = 0
for i in range(10):
    lista.append(float(input('digite um numero real: ')))

    if lista[i] < 0:
        negativos += 1
    else:
        positivos.append(lista[i])

print(f'a quantidade de numeros negativos é {negativos}\n e a soma dos positivos é {sum(positivos)}')
