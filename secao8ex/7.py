def convert(c):
    fahrenheit = c*(9/5) + 32
    return fahrenheit
celsius = float(input('digite a temperatura em celsius: '))
print(f'a temperatura em fahrenheit é {convert(celsius)}')