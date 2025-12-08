'''
Auxiliando o Hacker Neo a Desvendar a Verdade Sobre a Realidade.

História da Matrix: Neo, um hacker talentoso, vive uma vida dupla. No mundo que ele conhece, ele é um programador comum. Mas, e se existisse uma realidade escondida, uma verdade que ele nunca imaginou?
Após ser contatado por Morpheus, Neo se depara com uma escolha crítica: tomar a pílula vermelha e desvendar a verdade, ou tomar a pílula azul e continuar vivendo sua vida como sempre.

Fases do Programa:

Fase 1: A Escolha
- Neo deve escolher entre a pílula vermelha e a pílula azul. A escolha é feita através de um input do usuário:
    - Se o usuário digitar “vermelha”, Neo avança para a fase 2.
    - Se o usuário digitar “azul”, Neo continua vivendo sua vida normal e o programa termina.

Fase 2: Desvendando a Realidade
- Neo precisa questionar a realidade em que vive. Ele deve responder a três perguntas:
    - A realidade que você conhece é real? (Sim ou Não)
    - Existe uma realidade escondida? (Sim ou Não)
    - Você quer desvendar a verdade? (Sim ou Não)

Fase 3: Explorando a Verdade
- Se Neo responder “Sim” a todas as perguntas da fase 2, ele terá acesso a informações sobre a verdade, e o programa termina com uma mensagem de sucesso.
- Se Neo responder “Não” a qualquer uma das perguntas da fase 2, ele continua vivendo sua vida normal, e o programa termina com uma mensagem de que a escolha é dele.
'''

def main():
    # Leitura dos dados do usuário
    neo = input().split()

    # Desvendando a Matrix (Conclusão do exercício)
    if neo[0].lower() == "vermelha" and neo[1].lower() == "sim" and neo[2].lower() == "sim" and neo[3].lower() == "sim":
      print("Neo terá acesso a informações sobre a verdade.")
    elif neo[0].lower() == "vermelha":
        print("A escolha é sua, Neo continua vivendo sua vida normal.")
    else:
        print("Neo continua vivendo sua vida normal.")        

if __name__ == "__main__":
    main()