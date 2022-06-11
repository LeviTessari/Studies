from time import sleep
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
fin = float(input('Quantos anos de financiamento? '))

mes = fin*12
par = casa / mes
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, fin, par))
sleep(0.5)
if par < 0.3*salario:
    print('Emprestimo pode ser \033[32mCEDIDO\033[m !')

else:
    print('Empréstimo \033[31mNEGADO\033[m !')