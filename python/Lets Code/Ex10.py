from time import sleep
from itertools import count
numeros = []
notas = []
#notas = ['HH', 'QQQQ', 'XXXTXTEQH', 'W', 'HW']
teste = []
nota = 'WHQESTX'

def conta(teste):
    cont = 0
    for i in nota:
        numeros.append(teste.count(i))
        cont = cont + 1
    return numeros
def resul():
    resultado = (1 * numeros[0]) + ((1 / 2) * numeros[1]) + ((1 / 4) * numeros[2]) + ((1 / 8) * numeros[3]) + (
                (1 / 16) * numeros[4]) + ((1 / 32) * numeros[5]) + ((1 / 64) * numeros[6])
    return resultado
def confirmar():
    if resul() != 1:
        a = '\033[33mINCORRETO!\033[m'
        return a
    else:
        a = '\033[32mCORRETO!\033[m'
        return a
print('Bem vindo ao Programa de Duração de compasso.\n'
      'Avaliarei seu compasso e vou te falar se está de acordo com jingles.\n'
      'Lembrando que jingles possuem duração de 1 compasso.\n')
notas.append(input('Digite seu primeiro jingle: ').upper())
while True:
    b = input('Você quer validar outro jingle? [S/N] ').upper()
    if b[0] == 'S':
        notas.append(input('Digite o outro jingles: ').upper())
        continue
    elif b[0] == 'N':
        break
    else:
        print('Comando inválido, digite sim ou não.')
        continue
for k in range(0, len(notas)):
    for i in nota:
        for j in notas[k]:
            if i == j:
                teste.append(j)
    conta(teste)
    print(f'Para o compasso {notas[k]} foi obtido uma duração de {resul()}, portanto ele está {confirmar()}')
    teste.clear()
    numeros.clear()

    sleep(1)
print('Obrigado por utilizar meu serviço e até a próxima.')