def triangulo(n):
    
    for i in range(1, n+1): 
        print('*'*i)
        
        if i == n: # quando o i chegar na quantidade maxima da largura do triangulo
            qtd = i - 1
            
            for j in range(1, n+1): 
                print('*'*qtd)
                qtd -= 1

    
qtd = int(input('digite a quantidade de simbolos para compor o triangulo: '))
triangulo(qtd)
