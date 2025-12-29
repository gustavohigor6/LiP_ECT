'''
Gerador de Senhas Aleatórias

Você foi contratado para desenvolver um sistema simples que gere senhas seguras para usuários. Cada senha deve conter letras maiúsculas, letras minúsculas e números. Para facilitar a criação de várias senhas, o sistema deve gerar um conjunto de senhas automaticamente.

Importante: a semente deve ser definida com random.seed(42) antes de qualquer chamada a funções como random.choices() ou random.shuffle(). Isso garante que todos os alunos gerem exatamente as mesmas senhas.

Requisitos:
- Cada senha deve conter:
    - 3 letras maiúsculas
    - 3 letras minúsculas
    - 3 dígitos
- A senha deve ter 9 caracteres no total, dispostos em ordem aleatória.
- Utilize um laço de repetição para gerar a quantidade (qtd) de senhas desejada.
- Use o módulo random e defina a semente com random.seed(42) antes de gerar qualquer senha.

Dicas:
- import string pode ser útil
- Use string.ascii_uppercase, string.ascii_lowercase e string.digits para acessar letras e números.
- Use random.choices(..., k=3) para sortear 3 caracteres de uma lista.
- Por fim, use random.shuffle(lista) para embaralhar a ordem dos caracteres da senha.
'''
import random
import string

def main():
    # Leitura da quantidade de senhas a gerar
    qtd = int(input())

    random.seed(42)

    print(f"Gerando {qtd} senhas...")

    # Geração das senhas
    for _ in range(qtd):
        maiusculas = random.choices(string.ascii_uppercase, k=3)
        minusculas = random.choices(string.ascii_lowercase, k=3)
        numeros = random.choices(string.digits, k=3)
        lista = maiusculas + minusculas + numeros

        random.shuffle(lista)

        senha = "".join(lista)

        print(senha, end=' ')


if __name__ == "__main__":
    main()