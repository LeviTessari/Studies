frase = str(input('Digite uma frase: ')).strip().upper()


print('A frase possui {} de letras A.' .format(frase.count('A')))
frase2 = (''.join(frase.split()))
print('A primeira letra A está na posição {} e representa a {} letra escrita.'.format(frase.find('A'), frase2.find('A')+1))
print('A última letra A está na posição {} e representa a {} letra escrita'.format(frase.rfind('A'), frase2.rfind('A')+1))