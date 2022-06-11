import random

nome1 = input('Primeiro nome: ')
nome2 = input('Secundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')

lista = [nome1, nome2, nome3, nome4]
escolhe = random.choice(lista)

print(random.choice([f'{nome1}', f'{nome2}', f'{nome3}', f'{nome4}']))
print('{}'.format(escolhe))