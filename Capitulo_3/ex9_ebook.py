'''
Você é um fotógrafo profissional. Durante um trabalho, você se depara com um lago cristalino cercado por imensas montanhas. Seu objetivo é capturar uma foto aérea épica do lago, utilizando um drone. Para garantir a melhor perspectiva, você precisa determinar a altura ideal de voo do drone. Para isso, será necessário saber a distância horizontal entre você e a margem do lago, bem como a altura vertical que deseja alcançar com o drone.

A hipotenusa, que representa a distância diagonal percorrida pelo drone, pode ser calculada utilizando o Teorema de Pitágoras:
Hipotenusa = (Cateto Adjacente² + CatetoOposto²)^(1/2)

Seu programa receberá como entrada, em metros, o comprimento do cateto adjacente e do cateto oposto, e calculará a hipotenusa correspondente.
'''

def main():
    # Leitura dos dados do usuário
    catetos = list(map(int, input().split()))

    # Cálculo da hipotenusa + Conclusão do exercício
    hipotenusa = (((catetos[0] ** 2) + (catetos[1] ** 2)) ** 0.5)
    print(f"{hipotenusa:.2f} metros")

if __name__ == "__main__":
    main()