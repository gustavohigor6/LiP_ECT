'''
Escreva um programa que compare duas strings fornecidas pelo usuário, considerando valores booleanos "True"ou "False". O programa deve ignorar diferenças de capitalização (maiúsculas e minúsculas) e imprimir na tela se as strings são iguais ou diferentes .
'''

def main():
    # Recebendo as strings do usuário
    str1 = input("Insira a primeira palavra ou frase: ")
    str2 = input("Insira a segunda palavra ou frase: ")

    # Tratamento das strings e conclusão da atividade
    str1 = str1.lower()
    str2 = str2.lower()
    
    analise = str1 == str2

    print(analise)

if __name__ == "__main__":
    main()