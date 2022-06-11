c = 0
frase = str(input('Digite o palíndromo: ')).strip().upper()
frase1 = ''.join(frase.split())
frase2 = frase1[::-1]
n = int((len(frase1)-1)/2)
for i in range(0, n+1):
    if frase1[i] == frase2[i]:
        c += 1
if c == n+1:
    print('A palavrao {} que possui sua fraser inversa {} é um Palíndromo.'.format(frase, frase2))
else:
    print('Não é um Palíndromo')

#professor
for letra in range(len(frase1)-1, -1, -1): # vc escreve invertido usando for. [ qntidade iniial, final inversido, andar invertido
    inverso += frase1[letra]

if frase1 == frase2