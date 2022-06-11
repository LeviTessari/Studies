from time import sleep
print('Bom dia, estamos felizes em saber que deseja viajar conosco! Aqui podemos te informar quanto custa as passagens !')
km = float(input('Qual a distância em quilometros para onde você pretende viajar: '))
sleep(1)
if km <= 200:
    preco1 = km*0.5
    print('O valor de sua viagem será de R${:.2f}.'.format(preco1))
else:
    preco2 = km*0.45
    print('O valor da sua viagem será de R${:.2f}.'.format(preco2))
print('Agradecemos o interesse, gostaria de verificar outros valores?')