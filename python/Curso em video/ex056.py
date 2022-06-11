s = 0
conta = 0
velho = 0
homemvelho = ''
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    s += idade
    media = s/4
    if p == 1:
        if sexo == 'M':
            velho = idade
            homemvelho = nome
        elif sexo == 'F':
            if idade < 20:
                conta += 1
    else:
        if sexo == 'M':
            if idade > velho:
                velho = idade
                homemvelho = nome
        elif sexo == 'F':
            if idade < 20:
                conta += 1
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, homemvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(conta))