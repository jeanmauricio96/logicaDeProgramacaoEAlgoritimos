estoque = []  # Lista para armazenar as peças cadastradas
contador = 0  # Contador para gerar o código da peça

def cadastrarPeca():
    global contador
    contador += 1  # Incrementa o contador para gerar o código da próxima peça
    
    print('Código da Peça', str(contador).zfill(3))  # Exibe o código da peça (preenchido com zeros à esquerda)
    nome = input("Por favor entre com o NOME da peça: ")
    fabricante = input("Por favor entre com o FABRICANTE da peça: ")
    valor = float(input("Por favor entre com o VALOR(R$) da peça: "))

    # Cria um dicionário para representar a peça com os dados informados
    peca = {
        'codigo': str(contador),
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }

    estoque.append(peca)  # Adiciona a peça ao estoque

def consultarPeca():
    while True:
        print("\nEscolha a opção desejada:")
        print("1) Consultar Todas as Peças")
        print("2) Consultar Peças por Código")
        print("3) Consultar Peças por Fabricante")
        print("4) Retornar")

        opcao = input()  # Solicita a opção desejada ao usuário

        if opcao == "1":
            print("\n--- Todas as Peças ---")
            for peca in estoque:
                # Exibe as informações de cada peça
                print(f"Código: {peca['codigo']}")
                print(f"Nome: {peca['nome']}")
                print(f"Fabricante: {peca['fabricante']}")
                print(f"Valor: R${peca['valor']:.2f}")
                print("---------------------")

        elif opcao == "2":
            codigo = input("Digite o código da peça: ")
            for peca in estoque:
                if peca['codigo'] == codigo:
                    # Exibe as informações da peça com o código especificado
                    print("\n--- Peça Encontrada ---")
                    print(f"Código: {peca['codigo']}")
                    print(f"Nome: {peca['nome']}")
                    print(f"Fabricante: {peca['fabricante']}")
                    print(f"Valor: R${peca['valor']:.2f}")
                    break
            else:
                print("Peça não encontrada.")

        elif opcao == "3":
            fabricante = input("Digite o fabricante da peça: ")
            print("\n--- Peças do Fabricante ---")
            for peca in estoque:
                if peca['fabricante'] == fabricante:
                    # Exibe as informações das peças do fabricante especificado
                    print(f"Código: {peca['codigo']}")
                    print(f"Nome: {peca['nome']}")
                    print(f"Valor: R${peca['valor']:.2f}")
                    print("---------------------")

        elif opcao == "4":
            break  # Retorna para o menu principal

        else:
            print("Opção inválida. Digite novamente.")

def removerPeca():
    codigo = input("Digite o código da peça que deseja remover: ")
    for peca in estoque:
        if peca['codigo'] == codigo:
            estoque.remove(peca)  # Remove a peça do estoque
            print("Peça removida do estoque.")
            break
    else:
        print("Peça não encontrada.")

# Função principal do programa
def main():
    while True:
        print("Escolha a opção desejada:")
        print("1) Cadastrar Peças")
        print("2) Consultar Peças")
        print("3) Remover Peças")
        print("4) Sair")

        opcao = input()  # Solicita a opção desejada ao usuário

        if opcao == "1":
            print("Você selecionou a Opção de cadastrar Peças")
            cadastrarPeca()
        elif opcao == "2":
            print("Você selecionou a Opção de Consultar Peças")
            consultarPeca()
        elif opcao == "3":
            print("Você selecionou a Opção de Remover Peças")
            removerPeca()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    identificador = 'Jean Maurício Santos de Souza'
    RU = 4040623
    print("Bem Vindo ao Controle de Estoque da Bicicletaria do ", identificador, RU)
    main()