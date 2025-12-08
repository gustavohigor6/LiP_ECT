'''
Você é um biólogo trabalhando em um parque natural e está encarregado de monitorar três espécies de aves migratórias. Cada espécie tem um conjunto de ilhas preferidas para nidificação durante a temporada de migração. As preferências das espécies são as seguintes:

- Espécie 1: Prefere as ilhas com IDs de 1 a 10.
- Espécie 2: Prefere as ilhas com IDs de 6 a 17.

Algumas ilhas são compartilhadas entre as espécies, o que pode levar à competição por recursos. Seu trabalho é identificar quais ilhas são compartilhadas para implementar medidas de conservação. Dessa forma, dada uma entrada do usuário correspondente ao ID de uma das ilhas, verifique se essa ilha específica é uma área de competição ou se é exclusiva de uma das espécies.
'''

def main():
    # Leitura da ilha informada pelo usuário
    ilha = int(input())

    # Construção dos conjuntos ilhas
    ilha_esp_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    ilha_esp_2 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
    ilha_compartilhada = (ilha_esp_1 & ilha_esp_2)

    # Conclusão do exercício
    if ilha in ilha_compartilhada:
        print(f"Ilha {ilha} é compartilhada entre espécie(s):1 2.")
    elif ilha in ilha_esp_1 and ilha not in ilha_esp_2:
        print(f"Ilha {ilha} é exclusiva da Espécie 1.\nPortanto, não é compartilhada com outras espécies.")
    else:
        print(f"Ilha {ilha} é exclusiva da Espécie 2.\nPortanto, não é compartilhada com outras espécies.")


if __name__ == "__main__":
    main()