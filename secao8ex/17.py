def SomaEntre(a, b):
    soma = 0
    
    if a // 1 == a and b // 1 == b:

        if a >= b:
            
            for i in range(b+1, a,1):
                soma += i
                
        elif b >= a:
            
            for i in range(a+1, b,1):
                soma += i               
        
        return soma

a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))

print(f'o valor da soma entre os numeros é {SomaEntre(a, b)}')
    