'''
Escreva um programa que solicite ao usuário a inserção de duas coordenadas (x e y). Em seguida, crie uma tupla chamada coordenadas com esses valores e imprima o conteúdo da tupla na tela.
'''

def main():
    # Solicitando ao usuário as duas coordenadas
    coordenada_x = float(input("Insira a coordenada X: "))
    coordenada_y = float(input("Insira a coordenada Y: "))

    # Criação da tupla com a inserção dos dados
    coordenadas = (coordenada_x, coordenada_y)

    # Conclusão do exercício
    print(f"Coordenadas: {coordenadas}")


if __name__ == "__main__":
    main()