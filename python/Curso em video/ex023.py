#Meu jeito doido
num = int(input('Digite um numero: '))

numero = '{0:04}'.format(num)
print('Analisando o número {}'.format(num))
print('Unidade: {:4}'. format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))

#Professor
# A sacada foi faz a divisão inteira pelo // e depois vc faz a divisão e pega o resto usando o %
num = int(input('Digite um numero: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'. format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
