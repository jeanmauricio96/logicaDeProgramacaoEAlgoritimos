identificador='Jean Maurício Santos de Souza'
RU=4040623
# Imprime o cabeçalho da lanchonete com base no identificador fornecido.
print('''Bem Vindo a Lanchonete do'''+ identificador, RU + '\n' + 
'''****************Cardápio******************
| Código |        Descrição      | Valor |
|   100  |    Cachorro Quente    |  9,00 |
|   101  | Cachorro Quente Duplo | 11,00 |
|   102  |         X-Egg         | 12,00 |
|   103  |       X-Salada        | 12,00 |
|   104  |        X-Bacon        | 14,00 |
|   105  |        X-Tudo         | 17,00 |
|   200  |   Refrigerante Lata   |  5,00 |
|   201  |      Chá Gelado       |  4,00 |''')

# Dicionário que mapeia os códigos de produto para suas descrições e valores.
produtos = {
    100: {"Descrição": "Cachorro Quente", "Valor": 9.00},
    101: {"Descrição": "Cachorro Quente Duplo", "Valor": 11.00},
    102: {"Descrição": "X-Egg", "Valor": 12.00},
    103: {"Descrição": "X-Salada", "Valor": 13.00},
    104: {"Descrição": "X-Bacon", "Valor": 14.00},
    105: {"Descrição": "X-Tudo", "Valor": 17.00},
    200: {"Descrição": "Refrigerante Lata", "Valor": 5.00},
    201: {"Descrição": "Chá Gelado", "Valor": 4.00}
}

# Variável para armazenar o valor total do pedido.
valor_total = 0.0

# Loop principal para fazer pedidos até que o usuário decida sair.
while True:
    code = input("Entre com o código desejado (ou 'q' para sair): ")
    
    if code == "q":
        break
    
    code = int(code)

    # Verifica se o código de produto fornecido é válido.
    if code not in produtos:
        print("Opção Inválida")
        continue

    # Obtém as informações do produto com base no código fornecido.
    produto = produtos[code]
    valor_total += produto["Valor"]
    
    # Exibe a descrição e o valor do produto escolhido.
    print(f"Você pediu um {produto['Descrição']} no valor de R$ {produto['Valor']}")
    
    # Pergunta ao usuário se ele deseja fazer outro pedido.
    pedir_novamente = input('''Deseja mais alguma coisa? 
0 - Não 
1 - Sim
''')
    
    if pedir_novamente == "0":
        break
    elif pedir_novamente != "1":
        print("Opção inválida. Encerramos seu pedido!.")
        break

# Exibe o valor total a ser pago com base nos produtos selecionados.
print(f"O total a ser pago é: R$ {valor_total:.2f}")