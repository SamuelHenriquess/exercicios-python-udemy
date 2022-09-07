def fatorial(n):
    
    resultado = 1
    
    for i in range(1, n+1): # n+1 pro for rodar a quantidade certa de vezes
        resultado *= i  
    return resultado

num = int(input('digite o numero e descubra o seu fatorial: '))
print(fatorial(num))