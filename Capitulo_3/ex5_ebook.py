'''
Utilizando tuplas, você deve receber as coordenadas de um retângulo no plano cartesiano, onde (x_min, y_min) representa o canto inferior esquerdo e (x_max, y_max) representa o canto superior direito. Além disso, você tem um ponto representado por um par de coordenadas (x, y).

Sua tarefa é escrever um programa que determine se o ponto está dentro, tocando na borda ou fora do retângulo. O programa deve imprimir uma mensagem na saída padrão indicando o resultado da verificação.
'''

def main():
    # Leitura dos dados
    entrada = list(map(int, input().split()))
    
    # Separação correta dos pontos informados
    vetor_inicial = (entrada[0], entrada[1])
    vetor_final = (entrada[2], entrada[3])
    ponto = (entrada[4], entrada[5])

    # Determinação da posição do ponto informado + Conclusão do exercício
    if vetor_inicial[0] > ponto[0] or vetor_final[0] < ponto[0]:
        print("O ponto está fora do retângulo.")
    elif vetor_inicial[1] > ponto[1] or vetor_final[1] < ponto[1]:
        print("O ponto está fora do retângulo.")
    elif vetor_inicial[0] < ponto[0] and vetor_final[0] > ponto[0] and vetor_inicial[1] < ponto[1] and vetor_final[1] > ponto[1]:
        print("O ponto está dentro do retângulo.")
    else:
        print("O ponto está tocando a borda do retângulo.")
    

if __name__ == "__main__":
    main()