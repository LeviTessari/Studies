soma = i = valor = 0
Nome = ' '
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço do produto: R$'))
    soma += valor
    if valor > 1000:
        i += 1
    if i == 1:
        menor = valor
        Nome = nome
    if i != 1:
        if preço < menor:
            menor = preço
            Nome = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer cadastrar outro produto? [S/N] ' )).upper().strip()[0]
    if 'N' in resp:
        break
print(f'''  FIM DA COMPRAA  
O valor do gasto total é de : R${soma}.
Você comprou {i} produtos que custam mais de R$1.000!
O produto mais barato é {Nome} no valor de R${menor:.2f}''')