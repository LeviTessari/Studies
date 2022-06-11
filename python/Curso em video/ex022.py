#Meu método
nome = str(input('Digite seu nome completo: ')).strip() #O strip aqui já corta as laterais

print('Seu nome grandão é {}'.format(nome.upper()))
print('Seu nome pequenininho é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(''.join(nome.split()))))
#print('Seu nome possui {} letras'.format(nome.split()[0]+nome.split()[1])) ## << daria certo, mas eu preciso de um repetidor
print('Seu primeiro nome {} possui {} letras'.format(nome.split()[0], len(nome.split()[0])))

#Professor
nome = str(input('Digite seu nome completo: ')).strip() #O strip aqui já corta as laterais
print('Seu nome grandão é {}'.format(nome.upper()))
print('Seu nome pequenininho é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #Deste jeito ele simplesmente retirou a quantidade de espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #Deste jeito ele vai encontrar o primeiro espaço