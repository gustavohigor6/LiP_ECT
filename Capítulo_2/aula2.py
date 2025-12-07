def main():
    #Definindo variáveis
    '''
    nome = "Maria"

    #Formatando a Saída de Dados
    idade = 30
    #print("O nome dela é", nome, "e ela tem", idade, "anos.")
    #Separarador (sep)
    #print(nome, idade, sep=" - ")
    #Utilizando f-strings
    #print(f"O nome dela é {nome} e tem {idade} anos.")

    #Formatando Números Com Casas Decimais
    valor = 123.456789
    #print(f"O valor formatado é: {valor:.2f}")
    #Declaração e inicialização de uma variável do tipo inteiro
    x = 10
    #print(f"O valor de x é: {x}, e seu tipo é: {type(x)}")
    #Atribuição de um novo valor a uma variável do tipo inteiro
    x = 20
    #print(f"O valor de x é: {x}, e seu tipo continua sendo: {type(x)}")
    #Soma de dois inteiros
    resultado = x + 15
    #print(f"Somando 'x' com 15, temos como resultado: {resultado}\nSeu tipo é: {type(resultado)}")

    #Ponto flutuante (float)
    y = 3.14
    #print(f"O valor de y é: {y}\nSeu tipo é: {type(y)}")
    y = 2.5
    #print(f"O novo valor de y é: {y}\nSeu tipo continua sendo: {type(y)}")
    #Subtração de dois floats
    resultado1 = y - 9.3
    #print(f"Subtraindo 9,3 de 'y', temos como resultado: {resultado1:.1f}\nSeu tipo é: {type(resultado1)}")

    #Booleano
    a = True
    a = False
    #print(10 > 20)
    '''
    #Strings
    '''
    z = "Olá, turma!"
    #print(f"O valor de z é: {z}\nSeu tipo é: {type(z)}")
    z = "123"
    #print(f"O novo valor de z é: {z}\nSeu tipo continua sendo: {type(z)}")
    #Concatenação de strings
    resultado2 = z + ", como vai?"
    #print(f"O resultado da concatenação é: {resultado2}\nSeu tipo é: {type(resultado2)}")
    #Calcular o tamanho da string
    texto = 'Olá, turma!'
    tamanho_texto = len(texto)
    #print(f"O tamanho da string é: {tamanho_texto}")
    #Impressão de caracteres usando índices
    #print(f"Primeiro caractere: {texto[0]}")
    #print(f"Segundo caractere: {texto[1]}")
    #Impressão do último caractere usando índice -1
    #print(f"O último caractere é: {texto[-1]}")
    #Impressão de partes da string usando índices
    #print(f"Parte da string: {texto[4:9]}")
    #print("Parte da string:", texto[4:9])
    #Inverte a string
    #print(f"String invertida: {texto[::-1]}")
    #Função upper
    print(f"Aplicando o recurso .upper à string '{texto}', temos: '{texto.upper()}'")
    print(f"De maneira análoga, aplicando o recurso .lower à string original, temos: '{texto.lower()}'")
    '''
    #Dinamicidade de tipo
    #Atribuição dinâmica de valores
    '''
    variavel_dinamica = 25
    print(variavel_dinamica)
    variavel_dinamica = "Olá, mundo!"
    print(variavel_dinamica)
    #Declarando variáveis como None
    variavel_nula = None
    print(variavel_nula)
    #Atribuindo um valor posteriormente
    variavel_nula = 100
    print(variavel_nula)
    #Removendo uma variável existente
    del variavel_nula
    #print(variavel_nula)
    '''
    #Conversão de tipos e bases numéricas
    '''
    entrada_usuario = input("Digite um número de ponto flutuante: ")
    numero_float = float(entrada_usuario)
    print(f"Número de ponto flutuante digitado: {numero_float:.2f}")
    #Conversão entre bases numéricas em python
    numero_decimal = 9
    numero_binario = bin(numero_decimal)
    print(numero_binario) 
    numero_binario_2 = 0b1010 #Prefixo 0b indica o formato binário
    numero_decimal_2 = int(numero_binario_2)
    print(numero_decimal_2)
    numero_decimal_3 = 255
    numero_hexadecimal = hex(numero_decimal_3)
    print(numero_hexadecimal)
    numero_hexadecimal_2 = 0xff #Prefixo 0x indica o formato hexadecimal
    numero_decimal = int(numero_hexadecimal_2)
    print(numero_decimal)
    '''

    #Listas de dados compostos (Coleções)
    '''
    #Criação de listas:
    lista_vazia = []
    lista_vazia = list()
    numeros = [1, 2, 3]
    Acessando elementos da lista:
    
    linguagens = ["Python", "Java", "C++"]
    #print(linguagens[0])
    #print(linguagens[-1])
    print(linguagens) #Pré-atualização

    linguagens[1] = "Javascript"
    print(linguagens) #Realiza a impressão na tela de todos os itens da lista

    lista1 = [1, 2]
    lista2 = [3, 4]
    print(f"Lista 1 pré-atualizaçao {lista1}")
    print(f"Lista 2 {lista2}")
    lista1 += lista2
    print(f"Lista 1 pós-atualização {lista1}")
    print(f"Lista 2 {lista2}")
    '''
        #Criando lista de compras
    '''
    compras = ["Maçã", "Leite"]
    print(f"Primeira lista de compras: {compras}")

    compras.append("Pão")
    print(f"att.1 (append): {compras}")
    compras.extend(["Ovos", "Queijo"])
    print(f"att.2 (extend): {compras}")
    compras.insert(1, "Banana")
    print(f"att.3 (insert): {compras}")
    '''

    #Tuplas
    #São IMUTÁVEIS
        #Criação de Tuplas
    '''
    vazia = tuple()
    unitaria = (42,)
    coordenadas = (23.5, -46.6)

    ponto_a = (-23.55, -46.63) 
    ponto_b = (-22.91, -43.17)
    print(f"Rota: {ponto_a} -> {ponto_b}")

    cidades = {
        (-23.55, -46.63): "São Paulo",
        (-22.91, -43.17): "Rio de Janeiro"
    }
    print(f"A coordenada {ponto_a} representa a cidade {cidades[(-23.55, -46.63)]}")
    '''

    #Dicionários
    #São MUTÁVEIS, com dados no formato chave-valor.
        #Criação de Dicionários
    '''
    vazio = {}
    vazio1 = dict()

    cadastro = {
        "id": "user123",
        "ativo": False,
        "ultimo_acesso": "2023-10-15"
    }

    print(cadastro)
    cadastro["id"] = "user321"
    print(cadastro)
    '''
    
    #Conjuntos
        #Estruturas de dados que armazenam elementos únicos
    '''
    vogais = {'a', 'e', 'i', 'o', 'u'}
    numeros =  {1, 2, 3}
    numeros2 = {1, 3, 5}
    print(vogais, numeros)
    numeros.add(4)
    print(numeros)
    numeros.remove(2)
    print(numeros)
    numeros.discard(5)
    print(numeros)
        # Operações entre conjuntos #
        União
    print(numeros | numeros2)
        Interseção
    print(numeros & numeros2)
        Diferença
    print(numeros - numeros2)
        Os elementos devem ser imutáveis
    '''

    #Estruturas de Decisão
        #if / else / elif
    idade = 21
    if idade < 18:
        print("Você é menor de idade.")
    elif 18 <= idade < 65: #Forma pythonica
        print("Você é adulto")
    else:
        print("Você é um idoso.")

        #match case
    opcao = 2
    match opcao:
        case 1:
            print("Opção 1 selecionada")
        case 2:
            print("Opção 2 selecionada")
        case 3 | 4: #Combinação de padrões
            print("Opção 3 ou 4 selecionada")
        case _: #opção coringa, equivalente ao else
            print("Opção inválida")


if __name__ == "__main__":
    main()