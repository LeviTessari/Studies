soma = i = 0
while i != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        soma += n
        i += 1
    else:
        break
print(f'A soma dos {i} valores foi de {soma}.')

#Outro jeito
soma = 0
while True:
    num = int(input('Digie um valor igual allala'))
    if num == 999:
        break
    soma += num
print(soma)