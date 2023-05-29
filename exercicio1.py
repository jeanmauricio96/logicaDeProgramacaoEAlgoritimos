identificador = 'Jean Maurício Santos de Souza'
RU = 4040623

# Definição da função calculo_desconto_preco, que calcula o valor total, o valor com desconto e a porcentagem de desconto.
def calculo_desconto_preco(preco_unitario, quantidade):
    valor_total = preco_unitario * quantidade

    if quantidade < 10:
        desconto = 0
    elif 10 <= quantidade < 100:
        desconto = 0.05
    elif 100 <= quantidade < 1000:
        desconto = 0.1
    else:
        desconto = 0.15

    valor_desconto = valor_total - (valor_total * desconto)
    valor_porcentagem = desconto * 100
    return valor_total, valor_desconto, valor_porcentagem

# Impressão do cabeçalho da loja com base no identificador.
print("Bem vindo a loja do ", identificador, RU)

# Entrada do valor do produto e da quantidade.
preco_unitario = float(input("Entre com valor do produto: "))
quantidade = int(input("Entre com o valor da quantidade: "))

# Chamada da função calculo_desconto_preco para obter os valores calculados.
valor_total, valor_desconto, valor_porcentagem = calculo_desconto_preco(preco_unitario, quantidade)

# Impressão do valor total sem desconto.
print(f'Valor sem desconto foi: R$ {valor_total:.2f}')

# Impressão do valor com desconto e a porcentagem de desconto aplicada.
print(f'Valor com desconto foi: R$ {valor_desconto:.2f} (desconto {valor_porcentagem:.0f}%)')