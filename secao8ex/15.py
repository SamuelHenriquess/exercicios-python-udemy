def triangulo_check(a, b, c):
    
    if a <= (b + c):
        if b <= (a + c):
            if c <= (a + b):
                triangulo = True
                return triangulo
    return 'nao é um triangulo'

def tipo_triangulo(a, b, c):
    check = triangulo_check(a, b, c)
    if check:

        if a == b == c:
            return 'triangulo equilátero'
        
        elif ((a == b) and (b != c)) or ((b == c) and (c != a)):
            return 'triangulo isósceles'
        
        return 'triangulo escaleno'
    return 'valores inválidos'

lado1 = float(input('digite o primeiro lado do triangulo: '))
lado2 = float(input('digite o segundo lado do triangulo: '))
lado3 = float(input('digite o terceiro lado do triangulo: '))

print(f"\n{triangulo_check(lado1, lado2, lado3)}")
print(f"{tipo_triangulo(lado1, lado2, lado3)}")
