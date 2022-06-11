# Questão 6.
# Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
numeros = []
def soma(lista):
    som = 0
    for i in range(0, len(lista)):
        som = som + lista[i]
    return som
def executar():
    while True:
        a = int(input('Digite um número parar colocar na lista ou 0 para parar: '))
        if a == 0:
            break
        else:
            numeros.append(a)
executar()
print(f'Os números escolhidos são {numeros} e a soma deles é {soma(numeros)}')
