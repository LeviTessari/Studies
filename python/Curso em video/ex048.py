soma = 0
i = 0
for n in range(1, 501, 2):
    v = n % 3
    if v ==0:
        soma += n
        i += 1
print('A somatória de todos os {} números é o valor de {}.'.format(i, soma))
print(soma)
print(i)