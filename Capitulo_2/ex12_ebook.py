'''
Escreva um programa para coletar informações de um aluno. Utilizando um dicionário denominado “aluno”, solicite ao usuário as seguintes informações:
- Nome do aluno.
- Matrícula do aluno.
- Trẽs notas do aluno.

Posteriormente, exiba na tela os dados registrados, incluindo o nome, matrícula e a média das três notas do aluno. Utilize somente os métodos especiais dos dicionários para inserir e acessar os dados.
'''

def main():
    #Criação do dicionário + leitura dos dados informados pelo usuário
    inf = {
        "nome": None,
        "matricula": None,
        "notas": None
    }

    inf["nome"] = input()
    inf["matricula"] = input()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    # Cálculo da média + conclusão do exercício
    media = (nota1 + nota2 + nota3) / 3

    print(f"Nome: {inf["nome"]}\nMatrícula: {inf["matricula"]}\nMédia: {media:.1f}")


if __name__ == "__main__":
    main()