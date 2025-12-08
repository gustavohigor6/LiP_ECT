'''
Você deve criar um programa que verifica se os números em uma lista são pares ou ímpares. A lista possui tamanho 5 e será fornecida pelo usuário. Cada número na lista deve ser avaliado individualmente, sem o uso de estruturas de repetição (como loops). O programa deve exibir na tela se cada número é par ou ímpar.
'''

def main():
    # Leitura dos dados do usuário
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    # Conclusão do exercício com a criação da lista + tratamento de informações solicitadas
    lista = [num1, num2, num3, num4, num5]

    if lista[0] % 2 == 0:
        print(f"O número {lista[0]} é par.")
    else:
        print(f"O número {lista[0]} é impar.")

    if lista[1] % 2 == 0:
        print(f"O número {lista[1]} é par.")
    else:
        print(f"O número {lista[1]} é impar.")

    if lista[2] % 2 == 0:
        print(f"O número {lista[2]} é par.")
    else:
        print(f"O número {lista[2]} é impar.")
    
    if lista[3] % 2 == 0:
        print(f"O número {lista[3]} é par.")
    else:
        print(f"O número {lista[3]} é impar.")

    if lista[4] % 2 == 0:
        print(f"O número {lista[4]} é par.")
    else:
        print(f"O número {lista[4]} é impar.")


if __name__ == "__main__":
    main()