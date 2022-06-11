n = []
npar = []
nimpar = []
while True:
    a = int(input('Digite um valor: '))
    n.append(a)
    while True:
        b = str(input('Quer continuar? [S/N] '))
        if b[0].upper() in 'S':
            break
        if b[0].upper() in 'N':
            break
        else:
            print('Comando inválido!')
            continue
    if b[0].upper() in 'N':
        break

for c in range(0, len(n)):
    if n[c] % 2 == 0:
        npar.append(n[c])
    else:
        nimpar.append(n[c])

print('-='*30)
print(f'A lista completa é {n}\n'
      f'A lista de pares é {npar}\n'
      f'A lista de impares é {nimpar}')