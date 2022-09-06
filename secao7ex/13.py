lista = []

for i in range(5):
    lista.append(float(input('digite um valor: ')))

print(f' o maior valor é {max(lista)} e está na posição {lista.index(max(lista))+1}')
print(f' o menor valor é {min(lista)} e está na posição {lista.index(min(lista))+1}')
