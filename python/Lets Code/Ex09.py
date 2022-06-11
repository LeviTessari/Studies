#Crie (manualmente ou sorteando os números) uma lista de 10 números e imprima:
#1. uma lista com os 4 primeiros números;
#2. uma lista com os 5 últimos números;
#3. uma lista contendo apenas os elementos das posições pares;
#4. uma lista contendo apenas os elementos das posições ímpares;
#5. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da
#lista sorteada e termina com o primeiro);
#6. uma lista inversa dos 5 primeiros números;
#7. uma lista inversa dos 5 últimos números.
from random import randint
numeros = []
for i in range(0, 10):
    numeros.append(randint(0, 10))
a = numeros[:]
a.reverse()
print(f'Os números sorteados são: {numeros}\n'
      f'Os primeiro 4 números são: {numeros[0:4]}\n'
      f'Os 5 últimos são: {numeros[5:]}\n'
      f'Os elementos da posição par são: {numeros[::2]}\n'
      f'Os elementos da posição impar são: {numeros[1::2]}\n'
      f'A lista invertida é: {a}')

