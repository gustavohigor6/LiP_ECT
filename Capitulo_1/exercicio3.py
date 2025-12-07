def main():
    nomeCliente = input()
    produto = input()
    qtdProduto = input()
    valorProduto = input()

    print("Pedido confirmado:", produto)
    soma = int(qtdProduto) * float(valorProduto)
    print("Valor total: R$", soma)
    print("Obrigado pela preferência!")

if __name__ == "__main__":
    main()