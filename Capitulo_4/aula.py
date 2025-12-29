# Capítulo 4: Controle de Fluxo e Números Aleatórios

'''

__________________________________________________
- Estruturas de Decisão Aninhadas

Ex.:
idade = 25
sexo = "Feminino"

if idade >= 18:
    print("Você é maior de idade.")
    if sexo == "Feminino":
        print("E também do sexo feminino.")
else:
    print("Você é menor de idade.")

Saída: 
Você é maior de idade.
E também do sexo feminino.

__________________________________________________
- Estrutura de Repetição 'for'
# Gera uma lista com os números de 0 a 4
lista_numeros = list(range(5))

# Gera uma lista com números pares de 0 a 10
pares = list(range(0, 11, 2))
[0, 2, 4, 6, 8, 10]

for variavel in sequencia:
# A variável assume, em cada iteração, o valor de um elemento da sequência, e o bloco de código é executado para cada um desses valores

for i in range(5):
    print(i)

0
1
2
3
4

# Iterando sobre um dicionário

Utilizando o for para percorrer as chaves e valores de um dicionário:
alunos_notas = {
    "João: 8.5,
    "Maria": 9.0,
    "Pedro": 7.8
    }
for nome, nota in aluno_notas.items():
    print(f"{nome} obteve nota {nota}.")

# for aninhado

matriz = [
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
]

for linha in matriz:
    for numero in linha:
        print(numero, end=' ')
    print() # Pula para a próxima linha

# Outro exemplo de for aninhado

cores = ["vermelho", "azul", "verde"]
tamanhos = ["P", "M", "G"]

for cor in cores:
    for tamanho in tamanhos:
        print(f"{cor} - {tamanho}")

__________________________________________________
- Estrutura de repetição while

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

__________________________________________________
- Compreensões de Listas

[expressão for item in iterável if condição]

numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros]
print(quadrados) 

__________________________________________________
- Números aleatórios

import random

random.random() -> Retorna um número float aleatório entre 0 e 1
random.randint(a, b) -> Retorna um número int aleatório entre a e b
ranom.choice(seq) -> Retorna um elemento aleatório de uma sequência
random.sample(seq, k) -> Retorna uma amostra de k elementos aleatórios de uma sequẽncia
random.shuffle(seq) -> Embaralha a sequência original

__________________________________________________
- Definindo uma semente

Usado para reproduzir resultados específicos -> random.seed(valor)

