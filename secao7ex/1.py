a = [1,0,5,-2,-5,7] # cria uma lista
print(a) # printa a lista

soma = a[0] + a[1] + a[5] # armazena a soma de 3 posicoes em uma variavel(a)
print(soma) # printa a variavel

a.pop(4) # retira o elemento na posicao 4 para ser substituido
a.insert(4,100) # coloca o elemento 100 na posicao 4 completando a substituicao
print(a) # printa a lista 

for v in a: # pra cada elemento em lista 
    print(v) # printa esse elemento
