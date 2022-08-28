def positivo(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0
check = int(input('digite o numero a ser checado: '))
print(f'{positivo(check)}')