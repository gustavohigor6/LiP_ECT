#Questão 1
def ler_numeros():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    return n1, n2, n3

def encontrar_menor_maior(a, b, c):
    maior = max(a, b, c)
    menor = min(a, b, c)
    return menor, maior

#print(*ler_numeros(), sep=", ")

n1, n2, n3 = ler_numeros()
print(*encontrar_menor_maior(n1, n2, n3), sep=", ")



#Questão 2
def dobrar(numero: float):
    return numero * 2

def triplicar(numero: float):
    return numero * 3

def dividir_por_dois(numero: float):
    return numero / 2

def processar_e_somar_lista(operacao, lista_numeros):
    lista_nova = [ operacao(n) for n in lista_numeros ] #Entender essa parte seu merd@
    soma_todos = sum(lista_nova)
    return lista_nova, soma_todos
entrada = list(map(float, input().split()))

print(processar_e_somar_lista(dobrar, entrada)) #Executando uma função dentro de outra função

#ou ...

for funcao in [dobrar, triplicar, dividir_por_dois]:
    print(processar_e_somar_lista(funcao, entrada))