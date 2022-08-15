vetor = list(range(1,9)) # cria um vetor com 8 espacos
print(vetor)
for a in range(8): # passa o for 8 vezes
    vetor[a] = int(input("digite um valor: ")) # preenche o vetor na posicao de cada passa (1-8) com o valor especificado
print(vetor)

p1 = int(input("digite a primeira posicao: ")) # pergunta qual a primeira posicao
valor1 = vetor[p1] # atribui o primeiro valor para o mesmo da posicao adquirida
print(vetor)

p2 = int(input("digite a segunda posicao: ")) # pergunta a segunda posicao
valor2 = vetor[p2] # atribui o segundo valor para o mesmo da posicao adquirida
print(vetor)

soma = valor1 + valor2 # cria uma variavel que armazena o valor da soma 
print(soma) 
print(vetor)
