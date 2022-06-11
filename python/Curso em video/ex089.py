from time import sleep
classe = []
media = 0
#Registrar os alunos
while True:
     aluno = [str(input('Digite nome do aluno: ')), [float(input('Digite a nota 1: ')), float(input('Digite a nota 2: '))]]
     classe.append(aluno[:])
     aluno.clear()
     while True:
         b = str(input('Quer continuar? [S/N] '))
         if b[0].upper() in 'S':
             break
         if b[0].upper() in 'N':
             break
         else:
             print('Comando inválido!')
             continue
     if b[0].upper() in 'N':
         break
#Calcular a média dos alunos
for i in range(0, len(classe)):
    media = (classe[i][1][0] + classe[i][1][1])/2
    classe[i].append(media) #Colocando as médias em notas
#Aprovado ou reprovado
for i in range(0, len(classe)):
    if classe[i][2] >= 5:
        classe[i].append('APROVADO')
    else:
        classe[i].append('REPROVADO')
print(classe)
#Criação do layout do boletim
print('-='*25)
print(f'{"BOLETIM":^50}')
print('-='*25)
print(f'{"No.  ":<}{"NOME":^20}{"MÉDIA":^10}{"SITUAÇÃO":^10}')
print('-='*25)
for i in range(0, len(classe)):
    print(f'{i:<}    {classe[i][0]:^20}{classe[i][2]:^10}{classe[i][3]}')
print('-'*50)
#Análise individual de cada aluno
while True:
    a = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if a == 999:
        print('Finalizando...')
        sleep(1)
        print('Sistema encerrado. Volte sempre!')
        break
    print(f'Notas de {classe[a][0]} são {classe[a][1]}. O aluno está {classe[a][3]}!')