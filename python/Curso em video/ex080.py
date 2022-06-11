n = []
a = float(input('Digite um valor: '))
maior = menor = a
n.append(a)
print('Foi adicionaddo ao final da lista...')
for c in range(0,4):
    a = float(input('Digite um valor: '))
    if a > maior:
        n.append(a)
        maior = a
        print('Foi adicionaddo ao final da lista...')
    if menor < a < maior:
        if a >= (maior+menor)/2:
            n.insert(n.index(maior), a)
        if a < (maior+menor)/2:
            n.insert(n.index(menor)+1, a)
        print(f'Foi adicionado na posição {n.index(a)} da lista...')
    if a < menor:
        n.insert(0, a)
        menor = a
        print(f'Foi adicionado na posição {n.index(a)} da lista...')
    print(n)
print(f'Os valores digitados em ordem foram: {n}')
