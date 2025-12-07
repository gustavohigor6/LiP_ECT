'''
Faça um programa que calcula o Índice de Massa Corporal (IMC) de uma pessoa. O IMC é calculando dividindo-se o peso da pessoa pela sua altura ao quadrado. O IMC é uma medida da relação entre o peso e a altura de uma pessoa. O programa deve imprimir o IMC da pessoa, classificando-o de acordo com a tabela abaixo:
IMC | Classificação

< 18.5      | Abaixo do peso
18.5 - 24.9 | Saudável
25.0 - 29.9 | Sobrepeso
30.0 - 34.9 | Obesidade grau I
35.0 - 39.9 | Obesidade grau II
>= 40.0     | Obesidade grau III
'''

def main():
    # Recebendo as informações do usuário
    peso = float(input("Insira seu peso (em kg): "))
    altura = float(input("Insira sua altura (em metros): "))

    # Cálculo do IMC
    imc = (peso / (altura ** 2))

    # Conclusão da atividade
    if 18.5 > imc:
        print(f"Seu IMC é {imc:.2f} (Abaixo do peso).")
    elif 18.5 <= imc < 25.0:
        print(f"Seu IMC é {imc:.2f} (Saudável).")
    elif 25.0 <= imc < 30.0:
        print(f"Seu IMC é {imc:.2f} (Sobrepeso).")
    elif 30.0 <= imc < 35.0:
        print(f"Seu IMC é {imc:.2f} (Obesidade grau I).")
    elif 35.0 <= imc < 40.0:
        print(f"Seu IMC é {imc:.2f} (Obesidade grau II).")
    elif 40.0 <= imc:
        print(f"Seu IMC é {imc:.2f} (Obesidade grau III).")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()