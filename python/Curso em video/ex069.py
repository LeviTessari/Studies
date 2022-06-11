menor = homem1 = mulher1 = homem2 = mulher2 = homem3 = mulher3 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade < 18:
        menor += 1
        if 'M' in sexo:
            homem1 += 1
        else:
            mulher1 += 1
    elif 20 > idade >= 18:
        if 'M' in sexo:
            homem2 += 1
        else:
            mulher2 += 1
    elif 'M' in sexo and idade >= 20:
        homem3 += 1
    elif 'F' in sexo and idade >= 20:
        mulher3 += 1
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if 'N' in q:
        break
print(f'''O total de pessoas com mais de 18 anos: {homem2+homem3+mulher2+mulher3}
O de homens cadastrados é {homem2+homem3+homem1}.
O total de mulheres com menos de 20 anos é {mulher2+mulher1}.
E o total de menores de idade é {menor}.''')