matriz = [[], [], []]
for i in range(0, 3):
    for c in range(0, 3):
        a = int(input(f'Digite um valor para [{i}, {c}]: '))
        matriz[i].append(a)
for b in range(0, 3):
    for d in range(0, 3):
        print(f'[ {matriz[b][d]} ]', end='')
    print('')