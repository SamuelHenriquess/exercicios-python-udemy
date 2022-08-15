a = list(range(0,6)) # cria a lista com 6 espaços
print(a)
for v in range(6): # passa o v 6 vezes
    a[v] = int(input("digite um valor: ")) # o a passa na posicao v (6 vezes) e atribui o valor na casa da lista
    
print(a)