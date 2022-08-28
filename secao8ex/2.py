def data(dia, mes, ano):
    
    meses = { # criando um dicionario, ao inves de usar if 
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'
    }

    mes = meses.get(mes) # metodo get para pegar o valor na posicao mes
    print(f"{dia} de {mes} de {ano}")
    

dia1 = int(input("digite o dia: "))
mes1 = int(input("digite o mes: "))
ano1 = int(input("digite o ano: "))

data(dia1, mes1, ano1)