lista = []

for i in range(5):
    lista.append(float(input('digite um valor: ')))

print(lista)
print(f'o maior valor é {max(lista)}')
print(f'o menor valor é {min(lista)}')
print(f'a media dos valores é {sum(lista)/ len(lista)}')
