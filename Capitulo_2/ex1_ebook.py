'''
Escreva um programa que solicita ao usuário dois valores, um do tipo inteiro (int) e outro do tipo ponto flutuante (float). Após receber esses valores como entrada, o programa deve atribuí-los a duas variáveis distintas e, em seguida, imprimir na tela o resultado das seguintes operações matemáticas:
- Soma dos dois valores
- Subtração do valor do tipo float pelo valor do tipo inteiro
- Multiplicação dos dois valores
- Divisão do valor do tipo inteiro pelo valor do tipo float
'''

def main():
    # Recebendo e atribuindo os valores em inputs diferentes
    valor_int = int(input("Insira um valor do tipo inteiro: "))
    valor_float = float(input("Insira um valor do tipo float: "))

    # Impressão das operações matemáticas propostas para os dois valores informados

    print(f"Soma: {abs(valor_int + valor_float):.1f}")
    print(f"Subtração: {(valor_float - valor_int):.1f}")
    print(f"Multiplicação: {(valor_int * valor_float):.1f}")
    print(f"Divisão: {(valor_int / valor_float):.1f}")

if __name__ == "__main__":
    main()
