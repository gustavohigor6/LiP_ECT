#random
'''
IMPORTANTE:
- Importar as bibliotecas necessárias;
- Entender como utilizar as sementes;
- Integrar o conteúdo com as estruturas de repetição (for, while)
'''
#rodar o jogo até aparecer o número 55
import random
random.seed(4)

jogador = 0
n_jogadas = 0
'''
    for i in range(10):
    random.seed(i)
    print(random.randint(1, 6), end=" ")
'''
while True:
    num = random.randint(1, 100)
    jogador += num
    n_jogadas += 1
    if num == 55:
        break

print(n_jogadas)
print(jogador)

#recursividade
'''
IMPORTANTE
- Utilizar o "def"
- Treinar condições de parada e a recursividade
'''
def fatorial(n): #5 = 5*4*3*2*1 = 120
    # condição de parada (para este caso, será o último produto da expressão acima)
    if n == 1:
        return 1
    #recursividade ()
    return n * fatorial(n-1)
print("--->", fatorial(5))

#funções
def nome_da_funcao(n1, n2):
    soma = n1 + n2
    dif = n1 - n2
    return soma, dif #Formatação como lista: return [soma, dif]
#pulo do gato
res_soma, res_dif = nome_da_funcao(10, 5)
print(res_soma, res_dif)

'''
IMPORTANTE
- Resolver a questão 5 do capítulo 4 (Cálculo do Fatorial)
'''