def soma(n):
    if n > 0:    
        alg = str(n)
        soma = 0

        for n in alg:
            soma += int(n)

        return soma
        
    return 'numero inválido'
            
numero = int(input('digite o numero: '))
print(soma(numero))
