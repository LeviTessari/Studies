import random

maior = None
menor = None
a = random.randrange(10)
b = random.randrange(10)
c = random.randrange(10)
d = random.randrange(10)
e = random.randrange(10)
tupla = (a, b, c, d, e)

for c in tupla:
    if maior is None or maior < c:
        maior = c
    if menor is None or menor > c:
        menor = c
print('-=' * 30)
print(f'Os números gerados foram: {tupla}')
print('-=' * 30)
print(f'O maior número é o {maior}')
print('-=' * 30)
print(f'O menor número é o {menor}')


print('-'*100)

numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n} ', end=' ')
print(f'\nO maior valer sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

