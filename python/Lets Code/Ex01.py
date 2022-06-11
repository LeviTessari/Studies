# Questão 1.
# Faça um programa que peça ao usuário um número e imprima todos os números de um até o
# número que o usuário informar.
# 💡 Exemplo:
# Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4 5.
from time import sleep
numero = int(input('Digite seu número que vou lhe informar todos os demais. Qual é seu número?\n'))
print('Obrigado, estou fazendo aqui para você, aguarde...')
sleep(1)
print('Os números que você pediu são: ', end='')
for i in range(0, numero+1):
    print(f'{i} ', end='')
print('')
print('Espero que esteja feliz com seus números, até logo!')
