valor = []
while True:
        a = int(input('Digite um valor: '))
        if a in valor:
            print('Valor duplicado ! Não será adicionado!')
        else:
            valor.append(a)
            print('Valor adicionado com sucesso!')
        while True:
            b = str(input('Você quer continuar? [S/N] '))
            if b[0].upper() == 'S':
                break
            if b[0].upper() == 'N':
                break
            else:
                print('Comando inválido!')
                continue
        if b[0].upper() in 'N':
                break
print('-='*20)
valor.sort()
print(f'Você adicionou os valores: {valor}')