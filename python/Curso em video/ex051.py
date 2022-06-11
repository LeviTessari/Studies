print('='*30)
print('     \033[33m10 TERMOS DE UMA PA\033[m     ')
print('='*30)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
for i in range(0, 10):
    ai = i*r+n
    print('O {} termo vale: {}.'.format(i+1, ai))