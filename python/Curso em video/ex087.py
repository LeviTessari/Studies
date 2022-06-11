matriz = [[], [], [], []]
somapar = somaterceira = maior = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))
print('-='*30)
print('Sua Matriz é dado por:')
for i in range(0, 3):
    for c in range(0, 3):
       print(f'[ {matriz[i][c]} ]', end='')
    print('')
for i in range(0, 3):
    for c in range(0, 3):
        if matriz[i][c] % 2 == 0:
            matriz[3].append(matriz[i][c])
for i in range(0, len(matriz[3])):
    somapar += matriz[3][i]
print(f'A soma de todos os pares {matriz[3]} é dada por {somapar}.')
for i in range(0, 3):
    somaterceira += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {somaterceira}.')
for i in range(0, 3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]
print(f'O maior valor da segunda linha é o número {maior}.')
print('-='*30)