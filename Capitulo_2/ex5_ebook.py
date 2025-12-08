'''
Crie um programa que solicite ao usuário a inserção de cinco frutas diferentes. Antes da leitura dos dados, crie uma lista vazia chamada frutas. Em seguida, armazene as frutas fornecidas pelo usuário nessa lista e, ao final, imprima a lista completa na tela.
'''

def main():
    # Criação da lista vazia
    frutas = []

    # Leitura das entradas do usuário
    print("Digite 5 frutas (separadamente com ENTER):")
    fruta1 = input()
    fruta2 = input()
    fruta3 = input()
    fruta4 = input()
    fruta5 = input()

    # Armazenando as frutas na lista vazia
    frutas.extend([fruta1, fruta2, fruta3, fruta4, fruta5])

    # Conclusão do exercício
    print(f"Lista de frutas: {frutas}")

if __name__ == "__main__":
    main()