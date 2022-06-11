termo1= int(input('Qual é o seu primeiro termo? '))
razao = int(input('Qual é a razão? '))
final = 0
i = 0
print('{} termo vale {}.'.format(1, termo1))

while final != (termo1 + razao*9):
    i += 1
    final = termo1 + razao*i
    print('{} termo vale {}.'.format(i+1, final))
