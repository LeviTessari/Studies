while True:
    print('=-'*10)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=-' * 10)
    if n < 0:
        break
    for i in range(1, 11):
        print('{} x {:2} = {}'.format(n, i , n*i))
print('Programa encerrado! Volte logo')