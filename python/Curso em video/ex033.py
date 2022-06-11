n1= float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print('O maior número é {}.'.format(n1))
    if n2>n3:
        print('O menor valor é {}'.format(n3))
    else:
        print('O menor valor é {}'.format(n2))

if n2 > n1 and n2 > n3:
    print('O maior número é {}.'.format(n2))
    if n1>n3:
        print('O menor valor é {}'.format(n3))
    else:
        print('O menor valor é {}'.format(n1))

if n3 > n2 and n3 > n1:
    print('O maior número é {}.'.format(n3))
    if n2>n1:
        print('O menor valor é {}'.format(n1))
    else:
        print('O menor valor é {}'.format(n2))


