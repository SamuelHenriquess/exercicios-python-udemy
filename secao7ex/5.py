vetor = list(range(1,11)) # cria o vetor com 10 posicoes 
print(vetor)

for a in range(0,10): # roda 10 vezes
    vetor[a] = int(input("digite um valor: ")) # preenche cada posicao com o valor especificado
print(vetor)

par = 0

for b in range(10): # roda 10 vezes
    
    verifica = vetor[b]%2 #  ve se o resto de cada posicao é 0
    
    if verifica == 0:
        par +=1 # se for 0 adiciona um para a variavel par
    

print(par)
