i = 0
soma = 0
while i != 999:
    numero = int(input('Digite um número: '))
    i += 1
    if numero == 999:
        print('Foram escolhidos {} números cujo a soma vale {}'.format(i-1, soma))
        i = 999
    else:
        soma += numero
