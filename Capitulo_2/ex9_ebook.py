'''
Faça um programa que solicite ao usuário a inserção de três números inteiros distintos para cada conjunto. Os conjuntos conjunto_a e conjunto_b devem ser criados utilizando a função set() e preenchidos com os números fornecidos pelo usuário, utilizando o método .add(). Em seguida, realize as seguintes operações e imprima os resultados:
- União: combinar os elementos únicos de ambos os conjuntos.
- Interseção: encontrar os elementos que estão presentes em ambos os conjuntos.
- Diferença: identificar os elementos que estão em conjunto_a, mas não em conjunto_b.
'''

def main():
    # Leitura dos dados
    num1_cj1 = int(input())
    num2_cj1 = int(input())
    num3_cj1 = int(input())

    num1_cj2 = int(input())
    num2_cj2 = int(input())
    num3_cj2 = int(input())

    # Criação dos conjuntos + inserção de seus valores
    conjunto_a = set()
    conjunto_b = set()

    conjunto_a.add(num1_cj1)
    conjunto_a.add(num2_cj1)
    conjunto_a.add(num3_cj1)

    conjunto_b.add(num1_cj2)
    conjunto_b.add(num2_cj2)
    conjunto_b.add(num3_cj2)

    # Conclusão do exercício com as operações propostas
    print(f"União: {conjunto_a | conjunto_b}")
    print(f"Interseção: {conjunto_a & conjunto_b}")
    print(f"Diferença: {conjunto_a - conjunto_b}")

if __name__ == "__main__":
    main()