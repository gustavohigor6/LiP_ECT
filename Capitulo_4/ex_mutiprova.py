#Questão 1
'''
lista_temp = list(map(float, input().split(",")))

frio = 0
agradavel = 0
quente = 0

for i in lista_temp:
    if i < 15.0 :
        print(f"{i}°C: Frio")
        frio += 1
    elif i >= 15.0 and i < 25.0 :
        print(f"{i}°C: Agradável")
        agradavel += 1
    else:
        print(f"{i}°C: Quente")
        quente += 1

print(f"Total Frio: {frio}")
print(f"Total Agradável: {agradavel}")
print(f"Total Quente: {quente}")
'''

#Questão 2
'''
lista_notas = list(map(float, input().split(",")))

aprovacoes = 0
reprovacoes = 0
media = 0
contagem_medias = 0

for i in lista_notas:
    media += i
    contagem_medias += 1

    if i >= 5.0:
        aprovacoes += 1
    else:
        reprovacoes += 1

resultado = media / contagem_medias

print(f"Número de Alunos Aprovados: {aprovacoes}")
print(f"Número de Alunos Reprovados: {reprovacoes}")
print(f"Média da Turma: {resultado:.2f}")
'''

#Questão 3

lista_numeros = list(map(int, input().split(",")))
lista_numeros_2 = []

numeros_invalidos = 0
bool_invalidos = False

print(lista_numeros)
print(lista_numeros_2)

for i in lista_numeros:
    bool_invalidos = False
    contador = i
    aux = i
    if i >= 0 and i < 15:
        while contador > 1:
            contador -= 1
            aux *= contador
    else:
        numeros_invalidos += 1
        bool_invalidos = True
    
    if aux == 0:
        aux = 1
    elif bool_invalidos == True:
        lista_numeros_2.append("X")
    else:
        lista_numeros_2.append(aux)

print(lista_numeros_2)
print(numeros_invalidos)
