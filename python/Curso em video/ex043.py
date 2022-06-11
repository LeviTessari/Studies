m = float(input('Massa em kg: '))
h = float(input('Altura em m: '))

imc = m/(h*h)
print('{:.2f}'.format(imc))
if imc < 18.5:
    p = 'abaixo do peso'
elif 18.5 <= imc < 25:
    p = 'peso ideal'
elif 25 <= imc< 30:
    p = 'sobre peso'
elif 30 <= imc < 40:
    p = 'obesidade'
else:
    p = 'obesidade morbida'
print('{}'.format(p))