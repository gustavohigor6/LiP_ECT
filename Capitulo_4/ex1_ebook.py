'''
Classificação Etária: Desenvolva um programa que recebe várias idades de usuários na entrada, todas separadas por espaços. Para cada idade, o programa deve imprimir a categoria correspondente de acordo com a seguinte escala:

Menor de idade -> Menos de 13 anos
Adolescente -> De 13 a 17 anos
Maior de idade -> De 18 a 59 anos
Idoso -> 60 anos ou mais
'''

def main():
    # Leitura das idades
    idades = list(map(int, input().split()))

    for i in idades:
        if i < 13:
            print("Menor de idade")
        elif 13 <= i <= 17:
            print("Adolescente")
        elif 18 <= i <= 59:
            print("Maior de idade")
        else:
            print("Idoso")

if __name__ == "__main__":
    main()