'''
Escreva um programa que solicita ao usuário um número inteiro positivo entre 100 e 1000. Em seguida, o programa deve calcular o resto da divisão desse número por 5, armazenar o resultado em uma variável chamada resto e imprimir este valor.

Certifique-se de que o programa lide adequadamente com entradas inválidas. Caso o usuário insira um número negativo ou fora do intervalo especificado, exiba a seguinte mensagem de erro: “Por favor, insira um número inteiro positivo entre 100 e 1000.
'''

def main():
    # Leitura do número informado pelo usuário
    num = int(input())

    # Verificação do número informado + Conclusão do exercício
    if 100 <= num <= 1000:
        resto = num % 5
        print(f"O resto da divisão de {num} por 5 é {resto}.")
    else:
        print("Por favor, insire um número inteiro positivo entre 100 e 1000.")


if __name__ == "__main__":
    main()