numero = [[], []]
for c in range(0, 7):
    a = int((input(f'Digite o {c+1}º número: ')))
    if a % 2 == 0:
        numero[0].append(a)
    else:
        numero[1].append(a)
for c in range(0, 2):
    numero[c].sort()
print('-='*20)
print(f'Os números pares digitados foram: {numero[0]}.\n'
      f'Os números ímpares digitados foram: {numero[1]}.')