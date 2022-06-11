
tupla = (int(input('Qual seu primeiro número: ')), int(input('Qual seu segundo número: ')), int(input('Qual seu terceiro número: ')), int(input('Qual seu quarto número: ')))
print(f'O valor nove apareceu {tupla.count(9)} vezes.')
if tupla.count(3) == 0:
    print('O valor 3 não apareceu nenhuma vez.')
if tupla.count(3) != 0:
    print(f'O valor 3 está na posição {tupla.index(3)+1}')
for c in tupla:
    if c % 2 == 0:
        print(f'Os valores pares digitados foram: {c}')