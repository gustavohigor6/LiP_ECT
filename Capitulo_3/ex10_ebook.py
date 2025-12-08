'''
Um artesão está trabalhando em duas peças: um cone de metal e um paralepípedo de madeira. Para ajudá-lo em seu projeto, você precisa desenvolver um programa que receba as informações de dimensões em cm desses objetos e calcule seus volumes e massas.

- Receber na entrada as seguintes informações para o cone: Altura e Raio.
- Em seguida, receber as informações para o paralepípedo: Altura, Largura e Comprimento.

Considerando as fórmulas matemáticas adequadas para calcular o volume de cada objeto:
- Volume do Cone = (1/3)*pi*r²*h
- Volume do Paralelepípedo = l * w * h

Calcule a massa de cada objeto, considerando que a densidade do metal é de 8 g/cm³ e a densidade da madeira é de 0,5 g/cm³. Qual dos dois objetos, cone ou paralepípedo, é mais pesado? Considere que eles possuem o mesmo peso se a diferença entre as massas for menor do que 5g.
'''

def main():
    # Leitura dos dados informados pelo usuário
    dados = list(map(float, input().split()))

    # Atribuição dos dados às dimensões dos objetos
    cone_altura = dados[0]
    cone_raio = dados[1]
    para_altura = dados[2]
    para_largura = dados[3]
    para_comprimento = dados[4]

    # Cálculo do volume dos objetos
    volume_cone = ((3.14159 * (cone_raio ** 2) * cone_altura) / 3)
    volume_para = (para_altura * para_comprimento * para_largura)

    # Cálculo da massa de cada objeto
    massa_cone = volume_cone * 8
    massa_para = volume_para * 0.5

    # Conclusão do exercício
    resultado = massa_cone - massa_para
    if 0 <= abs(resultado) <= 5:
        print("O paralelepípedo e o cone possuem o mesmo peso.")
    elif resultado > 5:
        print(f"O cone é mais pesado com {massa_cone:.1f}g.")
    else:
        print(f"O paralelepípedo é mais pesado com {massa_para:.1f}g.")

if __name__ == "__main__":
    main()