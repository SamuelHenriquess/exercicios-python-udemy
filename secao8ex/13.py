def operacao(a, b, simb):
    if simb == '+':
        return a + b
    elif simb == '-':
        return a - b
    elif simb == '*':
        return a * b
    elif simb == '/':
        return a / b
    return 'operação inválida'

num1 = float(input('digite o primeiro valor: '))
num2 = float(input('digite o segundo valor: '))
op = str(input('digite a operação que deseja: +, -, *, /: '))

print(operacao(num1, num2, op))
