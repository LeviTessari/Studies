produto = float(input('Digite preço do produto: '))
novopreço = produto*0.95
desconto = produto*0.05
print('O produto teve um desconto de 5%, ou seja, de {:.2f} reais!\nAgora este produto custará apenas {:.2f}'.format(desconto, novopreço))