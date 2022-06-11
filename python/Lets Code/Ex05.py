#Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
#assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
#sim ou não:
#1. Mora perto da vítima?
#2. Já trabalhou com a vítima?
#3. Telefonou para a vítima?
#4. Esteve no local do crime?
#5. Devia para a vítima?
#Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
#pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
#necessitando de outras investigações. Valores abaixo de 2 são liberados.
#No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
#você vai informar como a polícia o considera.
solucao = ['Assassino. PRENDA!', 'Cúmplice. PRENDA!', 'Suspeito. Deve fazer mais investigações', 'Liberado.']
contador = 0
numero = 1
perguntas = ['Mora perto da vítima?', 'Já trabalhou com a vítima?', 'Telefonou para a vítima?', 'Esteve no local do crime?', 'Devia para a vítima?']
for i in perguntas:
    resposta = input(f"""Pergunta número #{numero}
{i} [S/N]: """).upper()
    numero += 1
    while True:
        if resposta[0] == 'S':
            contador += 1
            break
        elif resposta[0] == 'N':
            break
        else:
            resposta = input('Invalido, digite novamente [S/N]: ')
if contador == 5:
    print(f'A pessoa é: {solucao[0]}')
elif contador == 4 or numero == 3:
        print(f'A pessoa é: {solucao[1]}')
elif contador == 2:
    print(f'A pessoa é: {solucao[2]}')
else:
    print(f'A pessoa é: {solucao[3]}')
