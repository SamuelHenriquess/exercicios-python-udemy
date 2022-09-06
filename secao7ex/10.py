notas = []
soma = 0

for a in range(15):
    nota = float(input('digite quanto o aluno tirou: '))
    soma = soma + 1
    notas.append(nota)

media = sum(notas) / len(notas)
print(f' a media da sala foi {media}')
