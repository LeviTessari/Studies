from math import trunc
#pegando da biblioteca math e importanto o trunc

num = float(input('Digite um número: '))
n = trunc(num)

#usando a biblioteca math
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, n))

#não usando a biblioteca math
print('{:.0f}'.format(num))

#usando a função int
print('{}'.format(int(num)))