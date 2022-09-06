def DesenhaLinha(qtd):
    if qtd / 1 == qtd:
        
        for i in range(qtd): # o for roda o tanto de vezes especifidada por qtd
            print('=', end='')
    
    else:
        print('valor invalido')

qtd = int(input('digite a quantidade de sinais de igual que serão mostrados na tela: '))
DesenhaLinha(qtd)
