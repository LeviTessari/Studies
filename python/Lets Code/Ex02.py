#Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
#dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
#esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
#alguns exemplo abaixo:
#💡 Entrada: 25.01 | Saída: (25,50]
#Entrada: 25.00 | Saída: [0,25]
#Entrada: 100.00 | Saída: (75,100]
#Entrada: -25.02 | Saída: Fora de intervalo
#📌 Lembrando que o [ ou ] representa que o valor está contido no intervalo, enquanto o ( ou
#) representa que o valor associado não está contido no intervalo. Em outras palavras, (75, 100]
#representa o intervalo que vai de maior que 75 (não incluindo o 75) até menor ou igual 100.

intervalo = ['[0,25]', '(25,50]', '(50,75]', '(75,100]']
numero = int(input('Digete um valor, eu te falarei qual intervalo ele está, qual seu número? '))
if 0 <= numero <= 25:
    print(f'Você escolheu o número {numero}, ele está no intervalor {intervalo[0]}')
elif 25 < numero <= 50:
    print(f'Você escolheu o número {numero}, ele está no intervalor {intervalo[1]}')
elif 50 < numero <= 75:
    print(f'Você escolheu o número {numero}, ele está no intervalor {intervalo[2]}')
elif 75 < numero <= 100:
    print(f'Você escolheu o número {numero}, ele está no intervalor {intervalo[3]}')
else:
    print(f'O número {numero} não esta em nenhum dos meus intervalos!')