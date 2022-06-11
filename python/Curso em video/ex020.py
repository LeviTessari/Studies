import random

n1 = input('nome 1: ')
n2 = input('nome 2: ')
n3 = input('nome 3: ')
n4 = input('nome 4: ')
n5 = input('nome 5: ')
lista = [n1, n2, n3, n4, n5]
escolhe = random.sample(lista, k=4)
# random.shuffle(lista) pode embaralhar também a lista e depois vc printa a lista!!!

print('{}'.format(escolhe))
