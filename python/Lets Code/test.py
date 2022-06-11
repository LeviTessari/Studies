notas = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16 , 'T': 1/32, 'X': 1/64}

digite =  input('Maestro, qual é o compasso?')

quantidade_incorretos = []
quantidade_corretos = 0



composicao_compasso = digite.strip('/').split('/')

for compasso in composicao_compasso:
    duracao_do_compasso = 0
    for nota in compasso:
        duracao_do_compasso += notas[nota]

if duracao_do_compasso == 1:
    quantidade_corretos += 1
else:
    quantidade_incorretos.append(compasso)

print('Qtd. de Corretos:', quantidade_corretos)
if len(quantidade_incorretos) > 0:
  print('Incorreto:', quantidade_incorretos)