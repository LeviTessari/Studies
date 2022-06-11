#Questão 4.
#Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
#a) o produto entre o dobro do primeiro e a metade do segundo.
#b) a soma entre o triplo do primeiro e o terceiro.
#c) o terceiro elevado ao cubo
numero = []
for i in range(0,2):
    numero.append(int(input('Digite os valores você quer utilizar: ')))
print(f"""Você digitou os valores {numero[0]} e {numero[1]}.
O produto entre o dobro do primeiro e a metade do segundo é: {(2*numero[0])* numero[1]/2}
A soma entre o triplo do primeiro e o segundo é: {3*numero[0]+numero[1]}
O segundo elevado ao cubo é: {numero[1]**3}
""")