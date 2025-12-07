def main():
    #Exemplo simples sobre soma
    a = 1
    b = 2
    soma = a + b
    print("Soma =", soma)
    #Primeira utilização de input
    nome = input("Qual é o seu nome? ")
    idade = input("Qual é a sua idade? ")
    print("Seu nome é:", nome)
    print("Você tem", idade, "anos.")
    #Soma de a com idade, convertendo a variável idade
    soma2 = int(idade) + a
    print("Soma da idade com a =", soma2)

if __name__ == "__main__":
    main()