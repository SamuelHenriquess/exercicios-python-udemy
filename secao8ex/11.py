def medias(n1, n2, n3, letra):
    
    if letra.lower() == 'a':
        mediaAritmetica = (n1 + n2 + n3)/3
        return mediaAritmetica

    elif letra.lower() == 'p':
        mediaPonderada = (n1 * 5 + n2 * 3 + n3 * 2) / 10
        return mediaPonderada
        
    return 'letra inválida'

nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))
nota3 = float(input('digite a terceira nota do aluno: '))

letraCalc = str(input('digite a letra para o calculo: '))

print(medias(nota1, nota2, nota3, letraCalc))