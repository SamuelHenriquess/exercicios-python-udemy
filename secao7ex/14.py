lista = []
iguais = []
contador = 0

for i in range(10):
    print(i)
    lista.append(float(input('digite um valor: ')))
    print(lista)
    print(iguais)
    print(i)
    if lista[i] in iguais:
        print('esse valor ja está na lista')
        contador += 1
        print(i)
    print(i)
    iguais.append(lista[i])
    print(iguais)

print(f'existem {contador} valores iguais nessa lista')
    