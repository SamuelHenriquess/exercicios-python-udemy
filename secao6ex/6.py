soma = 0
for n in range(1,11):
    num = int(input("digite um número "))
    if num < 0:
        n -= 1
    soma = soma + num
print(soma)
print(soma/10)