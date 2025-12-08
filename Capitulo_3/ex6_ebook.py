'''
Desenvolva um sistema de autenticação que utilize um dicionário chamado usuarios_senhas para armazenar os nomes e as senhas de dois usuários. O programa deve solicitar que o usuário insira seu nome de usuário e senha. Em seguida, o sistema deve verificar se as credenciais inseridas correspondem às armazenadas no dicionário. Se as credenciais estiverem corretas, o programa deve exibir uma mensagem de “Login bem-sucedido! Bem-vindo, usuário.”. Caso contrário, deve informar ao usuário “Acesso negado. Credenciais inválidas.”.

- Obs: Serão armazenados apenas três usuários.
'''

def main():
    # Criação do dicionário
    usuarios_senhas = {
        "user1": None,
        "user2": None,
        "user3": None,
        "pw1": None,
        "pw2": None,
        "pw3": None
    }

    # Leitura dos dados informados pelo usuário + Atribuição dos valores ao dicionário
    entrada = input().split()

    usuarios_senhas["user1"] = entrada[0]
    usuarios_senhas["user2"] = entrada[2]
    usuarios_senhas["user3"] = entrada[4]
    usuarios_senhas["pw1"] = entrada[1]
    usuarios_senhas["pw2"] = entrada[3]
    usuarios_senhas["pw3"] = entrada[5]

    # Verificação das credenciais + Conclusão do exercício
    login = entrada[6]
    senha = entrada[7]

    if login == usuarios_senhas["user1"] and senha == usuarios_senhas["pw1"]:
        print(f"Login bem-sucessido! Bem-vindo, {login}")
    elif login == usuarios_senhas["user2"] and senha == usuarios_senhas["pw2"]:
        print(f"Login bem-sucessido! Bem-vindo, {login}")
    elif login == usuarios_senhas["user3"] and senha == usuarios_senhas["pw3"]:
        print(f"Login bem-sucessido! Bem-vindo, {login}")
    else:
        print(f"Acesso negado. Credenciais inválidas.")

if __name__ == "__main__":
    main()