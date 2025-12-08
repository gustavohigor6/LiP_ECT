'''
Dada duas strings fornecidas pelo usuário, realize as seguintes operações e imprima os resultados:
- Transformar em maiúsculas: converta toda a primeira string para letras maiúsculas.
- Transformar em minúsculas: converta toda a segunda string para letras minúsculas.
- Concatenar as strings: combine a primeira e a segunda string em uma única string.
- Imprimir o resultado: exiba a string concatenada na tela.
'''

def main():
    # Leitura das strings do usuário
    string1 = input()
    string2 = input()

    # Operações propostas nas strings
    op_1 = string1.upper()
    op_2 = string2.lower()
    
    # Conclusão do exercício
    print(op_1)
    print(op_2)
    print(f"{op_1 + op_2}")


if __name__ == "__main__":
    main()
