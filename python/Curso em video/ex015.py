km = float(input('Quanto km foram percorridos pelo carro alugado? '))
dias = int(input('Quantos dias o carro foi alugado? '))

valorkm = km * 0.15
valordias = dias*60
valortotal = valorkm + valordias

print('O carro rodou {} km e esteve alugado por {} dias, portanto deverá pagar R${}.\nR${} referente aos quilometros percorridos e R${} referente aos dias'. format(km, dias, valortotal, valorkm, valordias))