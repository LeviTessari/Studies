c=0
n = int(input('Digite um número: '))
for i in range(1,n+1):
    if n % i == 0:
        print('\033[32m{}\033[m'.format(i), end=' ')
        c += 1
    else:
        print('\033[31m{}\033[m'.format(i), end=' ')
print('')
print('O número {} foi divisível {} vezes!'.format(n, c))

if c == 2:
    print('O número é PRIMO!')
else:
    print('O número NÃO É PRIMO!')
