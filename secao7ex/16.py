lista = []

for i in range(5):
    lista.append(int(input('digite um valor: ')))

cod = int(input('digite 1 se quer ver a lista, digite 2 se quer ver a lista em ordem reversa: '))

if cod == 0:
    exit()
elif cod == 1:
    print(lista)
elif cod == 2:
    print(lista[::-1])
else:
    print('codigo invalido!')
