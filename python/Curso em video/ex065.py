numero = int(input('Digite um número: '))
menor = numero
maior = numero
i = 1
soma = numero
media = soma / i
while i != 'N':
    parar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if parar == 'N':
        i = 'N'
    elif parar == 'S':
        numero = int(input('Digite um número: '))
        i +=1
        soma += numero
        media = soma / i
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print('''A média dos valores digitado vale: {:.2f}
Maior número é o {}.
Menor número é o {}.'''.format(media, maior, menor))