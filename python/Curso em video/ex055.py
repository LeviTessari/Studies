peso = float(input('O peso da 1ª pessoa: '))
P = peso
p = peso
for i in range(2, 6):
    peso = float(input('O peso da {}ª pessoa: '.format(i)))
    if peso > P:
       P = peso
    elif p > peso:
        p = peso
print('O maior peso lido foi {:.1f} kg'.format(P))
print('O menor peso lido foi {:.1f} kg'.format(p))

