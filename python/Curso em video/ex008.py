dist = float(input('Digite o valor em metros: '))
cm = dist*100
mili = dist/1000
mili1 = dist*10**(3)

print('O valor em metros escolhido é {} \nEm centímetros é dado por {} \nEm milimetros é dado por {} \n Vamos testa o {}'. format(dist, cm, mili, mili1))