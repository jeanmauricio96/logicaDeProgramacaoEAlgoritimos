identificador='Jean Maurício Santos de Souza'
RU=4040623
print("Bem vindo a companhia de Logistica ", identificador, RU)

# Define uma função para obter um valor float do usuário, exibindo uma mensagem e tratando exceções caso o valor digitado não seja numérico.
def obterFloatInput(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite um valor numérico válido.")

# Define uma função para obter as dimensões do objeto (altura, comprimento e largura) do usuário.
# Calcula o volume do objeto com base nas dimensões e retorna um valor correspondente às faixas de volume.
def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            volume = altura * comprimento * largura
            if volume < 1000:
                print("O volume do objeto é (em cm³): ", volume)
                return 10
            elif volume < 10000:
                print("O volume do objeto é (em cm³): ", volume)
                return 20
            elif volume < 30000:
                print("O volume do objeto é (em cm³): ", volume)
                return 30
            elif volume < 100000:
                print("O volume do objeto é (em cm³): ", volume)
                return 50
            elif volume > 100000:
                print("O volume do objeto é (em cm³): ", altura * comprimento * largura)
                print("Não aceitamos objetos com dimensões tão grandes")
            else:
                raise ValueError
        except ValueError:
            print("Você digitou alguma dimensão com valor não numérico")
            print("Por favor, entre com as dimensões desejadas novamente")
            
# Define uma função para obter o peso do objeto do usuário.
# Retorna um valor correspondente às faixas de peso.
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            elif peso > 30:
                print("Não aceitamos objetos tão pesados")
                print("Entre com o peso desejado novamente")
            else:
                raise ValueError
        except ValueError:
            print("Você digitou algum valor não numérico para o peso")
            print("Por favor, entre com o peso desejado novamente")

# Define uma função para selecionar a rota com base em um dicionário de rotas fornecido.
# Exibe as opções de rota para o usuário e retorna o multiplicador correspondente à rota selecionada.
def rotaObjeto(rotas):
    print("Selecione a rota:")
    for chave, valor in rotas.items():
        print(f"{chave}: {valor['Rota']}")

    while True:
        rota = input()
        if rota in rotas:
            return rotas[rota]["Multiplicador"]
        else:
            print("Você digitou uma rota que não existe")
            print("Por favor, entre com a rota desejada novamente")
            print("Selecione a rota:")
            for chave, valor in rotas.items():
                print(f"{chave}: {valor['Rota']}")

# Calcula o valor total com base nas dimensões, peso e rota selecionados.
def calcularValor(dimensoes, peso, rota):
    valor = dimensoes * peso * rota
    return valor

# Dicionário contendo as rotas e seus respectivos multiplicadores.
rotas = {
    'RS': {"Rota": "De Rio de Janeiro até São Paulo", "Multiplicador": 1},
    'SR': {"Rota": "De São Paulo até Rio de Janeiro", "Multiplicador": 1},
    'BS': {"Rota": "De Brasília até São Paulo", "Multiplicador": 1.2},
    'SB': {"Rota": "De São Paulo até Brasília", "Multiplicador": 1.2},
    'BR': {"Rota": "De Brasília até Rio de Janeiro", "Multiplicador": 1.5},
    'RB': {"Rota": "De Rio de Janeiro até Brasília", "Multiplicador": 1.5},
}

# Chama as funções para obter as dimensões, peso e rota do objeto.
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto(rotas)

# Calcula e exibe o valor total a ser pago com base nas dimensões, peso e rota selecionados.
valor_total = calcularValor(dimensoes, peso, rota)
print("Total a pagar (R$): ", valor_total, "(dimensões: ", dimensoes, "* peso: ", peso, "* rota: ", rota, ")")