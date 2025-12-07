'''
Escreva um programa que solicite ao usuário que insira uma palavra ou frase. Em seguida, o programa deve imprimir o comprimento da string, a primeira letra da string, a última letra da string e a string invertida.
'''

def main():
    # Solicitação da palavra ou frase
    str = input("Entre com uma palavra ou frase: ")

    # Tratamento da string informada em outras variáveis
    comprimento = len(str)
    primeira_letra = str[0]
    ultima_letra = str[-1]
    invertida = str[::-1]

    # Impressão das informações propostas pelo enunciado

    print(f"{comprimento}\n{primeira_letra}\n{ultima_letra}\n{invertida}")

if __name__ == "__main__":
    main()