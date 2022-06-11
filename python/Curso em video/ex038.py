#meu jeito
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo númeiro inteiro: '))

if n1 > n2:
    print('O primeiro valor é \033[32mmaior\033[m ! {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor  é \033[32mmaior\033[m ! {} é maior que {}'.format(n2, n1))
else:
    print('Os dois valores são \033[33miguais\033[m !')

