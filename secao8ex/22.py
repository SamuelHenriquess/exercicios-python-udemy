def geraLinha(n):
    for i in range(1,n+1):
        print('!'*i)

qtd = int(input('digite a quantidade de pontos de exclamação a serem gerados: '))
geraLinha(qtd)