nota1 = nota10 = nota20 = nota50 = resto = 0
print('='*30)
print('          BANCO CEV          ')
print('='*30)
valor = int(input('Qual valor você deseja sacar? R$'))
while True:
    if valor >= 50:
        nota50 = valor // 50
        resto = valor % 50
        valor = resto
    if 20 <= valor < 50:
        nota20 = valor // 20
        resto = valor % 20
        valor = resto
    if 10 <= valor < 20:
        nota10 = valor // 10
        resto = valor % 10
        valor = resto
    if 1 <= valor < 10:
        nota1 = valor // 1
        resto = valor % 1
    if resto == 0:
        break

while True:
    if nota50 > 0:
        print(f'Total de {nota50} cédulas de R$50.')
    if nota20 > 0:
        print(f'Total de {nota20} cédulas de R$20.')
    if nota10 > 0:
        print(f'Total de {nota10} cédulas de R$10.')
    if nota1 > 0:
        print(f'Total de {nota1} cédulas de R$1.')
    break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um excelente dia!')