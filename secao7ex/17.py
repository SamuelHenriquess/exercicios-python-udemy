lista = []

for i in range(10): 
    lista.append(float(input('digite um valor: ')))
    
    if lista[i] < 0:
        lista[i] = 0

print(lista)
