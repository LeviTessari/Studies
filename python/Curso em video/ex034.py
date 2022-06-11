salario = float(input('Digite o seu salário: '))
if salario > 1250:
    salario1 = salario*1.1
    print('Seu salário de R${:.2f} passou a ser de R${:.2f}'.format(salario, salario1))
else:
    salario1 = salario*1.15
    print('Seu salário de R${:.2f} passou a ser de R${:.2f}'.format(salario, salario1))