'''
Crie, antes da leitura dos números, um conjunto vazio chamado numeros utilizando a função set(). Em seguida, armazene os valores fornecidos pelo usuário nesse conjunto, utilizando o método .add(). Ao final, exiba o conjunto completo na saída.
'''

def main():
    # Criação do conjunto vazio
    numeros = set()

    # Leitura dos números fornecidos pelo usuário
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    # Adição dos números ao conjunto
    numeros.add(num1)
    numeros.add(num2)
    numeros.add(num3)
    numeros.add(num4)
    numeros.add(num5)

    # Conclusão do exercício
    print(numeros)

if __name__ == "__main__":
    main()