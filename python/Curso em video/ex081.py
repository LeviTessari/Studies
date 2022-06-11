n =[]

while True:
    a = int(input('Digite um valor: '))
    n.append(a)
    while True:
        b = str(input('Você quer continuar? [S/N] ')).split()
        if b[0].upper() in 'S':
            break
        if b[0].upper() in 'N':
            break
        else:
            continue
    if b[0].upper() in 'N':
        break
print('-='*30)
n.sort(reverse=True)
print(f'Você digitou {len(n)} elementos.')
print(f'Os valores em ordem decrescente são {n}')
if 5 in n:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
