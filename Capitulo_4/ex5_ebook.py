'''
Cálculo do Fatorial: Escreva um programa que receba uma lista de números inteiros, e obedecendo alguns critérios, calcule e imprima o fatorial de cada um deles. O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio número.

Aqui estão as etapas e critérios para implementar seu programa:

- Receba e armazene uma lista de números inteiros.
- Verifique se cada número é válido (ou seja, maior ou igual a zero e menor do que 15).
- Calcule o fatorial de cada número usando um loop for ou while.
- Exiba o resultado do fatorial para cada um dos números. Se não for possível calcular o fatorial (por exemplo, para números não válidos), escreva um X.
- Mostre a quantidade de números para os quais não foi possível calcular o fatorial.
'''

def main():
    # Leitura dos números
    numeros = list(map(int, input().split(',')))

    # Verificação dos números
    for i in numeros:
        num = None
        if 0 < i < 15:
            contador = i - 1
            num = i
            while contador >= 1:
                num *= contador
                contador -= 1
        elif i == 0:
            num = 1
        else:
            num = "X"
        print(f"{num},", end=' ')


if __name__ == "__main__":
    main()