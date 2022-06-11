print('='*15 + ' \033[33mLOJAS LEVIS\033[m ' + '='*15)

valor = float(input('Valor das compras: R$'))
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
op = int(input('Qual forma de pagamento? '))

if op == 1:
    valor1 = 0.9*valor
    print('O valor da compra será de R$ {:.2f}.'.format(valor1))
elif op == 2:
    valor1 = 0.95*valor
    print('O valor da compra será de R$ {:.2f}.'.format(valor1))
elif op == 3:
    valor1 = valor/2
    print('O valor da compra será duas parcelas de R$ {:.2f}.'.format(valor1))
elif op == 4:
    div = int(input('Quantos meses deseja parcelar? '))
    valor1 = (valor / div)*1.2
    print('O valor da compra será {} parcelas de R$ {:.2f}.'.format(div, valor1))
else:
    print('Número invalido.')
