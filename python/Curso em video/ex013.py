salário = float(input('Digite o salário do funcionario: R$'))
novo = salário*1.15
aumento = salário*0.15

print('O salário de {:.2f}, sofreu um aumento de {:.2f}! Agora receberá {:.2f}'. format(salário, aumento, novo))