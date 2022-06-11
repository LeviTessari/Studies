tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
digite = 'Digite um número entre 0 e 20: '

while True:
    numero = int(input(digite))
    if 0 <= numero <= len(tupla):
        print(f'Seu número se escreve: {tupla[numero]}')
        break
    else:
        print('Tente novamente.')


