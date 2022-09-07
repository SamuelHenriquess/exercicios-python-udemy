def primos(n):
    p = 0

    for i in range(1, n):
        cont = 0

        for j in range(1,i+1):
            if i%j == 0:
                cont += 1

        if cont <= 2:
            p += 1

    return p

num = int(input('digite o numero e descubra quantos primos existem abaixo dele: '))
print(f'a quantidade de primos abaixo de {num} é {primos(num)}')