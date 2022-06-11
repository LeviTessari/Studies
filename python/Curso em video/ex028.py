import random
import time
print("-=-"*30)
print('Vou pensar em um número entre 0 e 5! Tente adivinhar...')
print("-=-"*30)
numero = random.randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('Processando...')
time.sleep(1)
if numero == num:
    print('Parabéns, você conseguiu me vencer!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(numero, num))

print('Bora de novo?')