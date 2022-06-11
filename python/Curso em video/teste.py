lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) #ordem alfabetica

a = ( 2, 5, 4)
b = ( 5, 8, 1, 2)
c = b+a
print(c)
print(c.count(2))