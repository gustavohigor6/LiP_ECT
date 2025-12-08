'''
Escreva um programa que converta uma temperatura de Celsius para Fahrenheit.
Utilize a fórmula: F = 9/5 * C + 32
- Solicite ao usuário que digite a temperatura em Celsius.
- Em seguida, converta a temperatura digitada para Fahrenheit utilizando a fórmula fornecida.
- Por fim, exiba na tela o resultado da conversão para o usuário, formatado com 2 casas decimais.
'''

def main():
    # Leitura da temperatura (em Celsius)
    temp_c = float(input())

    # Conversão da temperatura
    temp_f = (9 / 5 * (temp_c) + 32)

    # Conclusão do exercício
    print(f"A temperatura em Fahrenheit é: {temp_f:.2f}")

if __name__ == "__main__":
    main()