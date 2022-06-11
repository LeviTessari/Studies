dado = []
pessoas = []
nomemaior = []
nomemenor = []
tot = maior = menor = 0
while True:
    dado.append(str(input('Digite nome da pessoa: ')), int(input('Digite o peso da pessoa: ')))
    pessoas.append(dado[:])
    dado.clear()
    tot +=1
    while True:
        a = str(input('Quer continuar? [S/N] '))
        if a[0].upper() in 'S' or 'N':
            break
        else:
            print('Comando inválido!')
            continue
    if a[0].upper() in 'N':
        break

maior = menor = pessoas[0][1]

for i in pessoas:
    if i[1] == maior:
        nomemaior.append(i[0])
    if i[1] > maior:
        nomemaior.clear()
        maior = i[1]
        nomemaior.append(i[0])
    if i[1] == menor:
        nomemenor.append(i[0])
    if i[1] < menor:
        nomemenor.clear()
        menor = i[1]
        nomemenor.append(i[0])
print(f'Foram registradas {tot} de pessoas.\n'
      f'A(s) pessoa(s) {nomemaior} possui o maior peso, equivalente a {maior} kg.\n'
      f'A(s) pessoa(s) {nomemenor} possui o menor peso, equivalente a {menor} kg.')