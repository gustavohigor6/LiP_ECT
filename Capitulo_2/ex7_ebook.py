'''
Crie um dicionário chamado contato. Solicite ao usuário que forneça os dados correspondentes às chaves "nome", "telefone" e "endereco". Em seguida, imprima o conteúdo completo do dicionário.
'''

def main():
    # Criação do dicionário + solicitação dos dados 'nome', 'telefone' e 'endereço'.
    dic = {
        "nome": "vazio",
        "telefone": "vazio",
        "endereco": "vazio"
    }
    dic["nome"] = input("Insira o nome: ")
    dic["telefone"] = input("Insira o telefone: ")
    dic["endereco"] = input("Insira o endereço: ")

    # Conclusão do exercício
    print(f"Nome: {dic["nome"]}, Telefone: {dic["telefone"]}, Endereço: {dic["endereco"]}.")


if __name__ == "__main__":
    main()