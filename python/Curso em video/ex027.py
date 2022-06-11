nome = str(input('Digite seu nome: ')).strip()
print('Prazer em te conhecer {} !'.format(nome))

print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))
print('Seu último nome é {}'.format(nome.split()[len(nome.split())-1]))