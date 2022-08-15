vetor = list(range(1,11)) # cria o vetor com 10 posicoes 
print(vetor)

for a in range(0,10): # roda 10 vezes
    vetor[a] = int(input("digite um valor: ")) # preenche cada posicao com o valor especificado
print(vetor)

maior = max(vetor) # armazena o maior valor em uma variavel
menor = min(vetor) # armazena o menor valor em uma variavel

print(maior)
print(menor)