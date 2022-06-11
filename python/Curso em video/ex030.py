n = int(input('Digite um valor e vamos te falar se é par ou impar: '))
m = n % 2

if m == 0:
    print('Número escolhido {} é um número PAR!'.format(n))
else:
    print('Número escolhido {} é IMPAR!'.format(n))

print('Viu como eu sei também?')