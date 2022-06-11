soma = 0
for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares são {}'.format(soma ))