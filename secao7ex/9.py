lista = []

for a in range(6):
    par = int(input('digite um numero par: '))
    if par % 2 == 0:
        lista.append(par)
    else:
        print("digite apenas numeros pares! \n")

print(lista[::-1])
