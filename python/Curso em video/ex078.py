valores = []
ExameValores = []

for qnt in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {qnt}: ')))
print('=-'*20)
print(f'Você digitou os valores {valores} \n')
ExameValores = valores[:]
ExameValores.sort()
print(f'O maior valor digitado foi {ExameValores[4]} nas posições: ', end='')
for maior in range(0, 5):
    if ExameValores[4] == valores[maior]:
        print(f'{valores.index(valores[maior], maior)} ', end='')
print('\n')
print(f'O menor valor digitado foi {ExameValores[0]} nas posições: ', end='')
for menor in range(0, 5):
    if ExameValores[0] == valores[menor]:
        print(f'{valores.index(valores[menor], menor)} ', end='')
print('\n')
print('=-'*20)