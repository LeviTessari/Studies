from time import sleep
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
c=0

while c != 5:
    sleep(1)
    c = int(input('''Bem vindo ao nosso cálculo do dia a diaa!!!
    Aqui está algumas opções de como podemos lhe ajudar!
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair
    '''))

    if c == 1:
        soma = n1 + n2
        print('A somatória dos números será {}: '.format(soma))
    elif c == 2:
        multiplica = n1 * n2
        print(' A multiplicação dos números será {}: '.format(multiplica))
    elif c == 3:
        if n1 > n2:
            print('O {} é o maior número!'.format(n1))
        else:
            print('O {} é o maior número!'.format(n2))
    elif c == 4:
        n1 = float(input('Novo primeiro número: '))
        n2 = float(input('Novo segundo número: '))
    elif c > 5:
        print('Número inválido, por favor digite outro.')
print('Obrigado por utilizar nosso serviço! Até breve.')