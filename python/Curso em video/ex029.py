vel = float(input('Qual a velocidade do carro? '))
limite = 80
taxa = 7
if vel > limite:
    multa = (vel - limite)*taxa
    print('MULTADO! Você excedeu o limite permitido que é de {} km/h.'.format(limite))
    print('Você deve pagar uma multa de R${:.2f}.'.format(multa))

print('Tenha um bom dia! Dirija com segurança !')