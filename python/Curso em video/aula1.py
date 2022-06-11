f = 'ABCDEFGHI'
a = ['AD', 'BE', 'CF', '']
s = len(a)
t = a[0]+a[1]
print(len(a))
print(a[0]+a[1])
print('João possui {} anos'.format(t))
print(f[0:4])
print(f[:6])
print(f[3:])

frase = 'Curso em Video Python'
#Identificar somente o 10 caracter
print(frase[9])
#Fatiar de no meio, Começar inicio e vai até um antes do final
print(frase[9:13])
#Fatiar pulando de dois em dois [inicio : final: pulando]
print(frase[9:21:2])
#Fatiar do inicio até um ponto [: final ]
print(frase[:5])
#Fatiando de um ponto até o final [ inicio:]
print(frase[15:])
print(frase[9::3]) #começa no 9 e vai ate o final pulando de 3 em 3
#----------Analise----------
#Ver a quantidade de caracter
print(len(frase))
#Conta quantas letras possui na frase
print(frase.count('o'))
#Contagem com fatiamento count('o', 0, 13)
print(frase.count('o', 0 ,13))
#Encontrar a frase e informa em qual parte que começa
print(frase.find('deo'))
print(frase.find('Androiod')) #Ele retorna -1, significando que ele não está presente
#Conferir se existe palavra dentro da frase
print('Curso' in frase)
#----------Transformação----------
#Substituição .replace(Palavra que esta, palavra que vai substituir)
print(frase.replace('Python', 'Android')) #Ele não altera a palavra definitivamente
#Transforma em maiusculo toda frase
print(frase.upper()) #Ele não altera a frase definitivamente
#Transforma em minusculo toda a frase
print(frase.lower())
#Transforma toda a frase em minusculo, menos a primeira
print(frase.capitalize())
#Transforma cada primeira letra das palavras em maiusculo
print(frase.title())
#Remove os espaços inuteis
frase = '   Aprenda Python  '
print(frase.strip())
#Variação .rstrip() para tirar somente lado direito
print(frase.rstrip())
#Variação .lstrip() para tirar somente lado esquerdo
print(frase.lstrip())
frase = 'Curso em Vídeo Python'
#Divisão onde possui espaço
print(frase.split()) #Gera uma lista com a divisão, onde cria elementos
#Junção de elementos de uma lista em uma frase só
print(frase.split('-'.join(frase)))

print('-'*10)
print(frase[::2])
print(frase.upper().count('O')) #Podemos combinar funções
print(frase.replace('Python', 'Androiod'))
frase = frase.replace('Python', 'Androiod')
print(frase)
print('Curso' in frase)
print(frase.lower().find('Vídeo'))
print(frase.title().split())
print(frase.title().split()[3][2])