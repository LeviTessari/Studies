PARE = ''
sexo = input('Digite o sexo da pessoa: ').upper().strip()
while sexo != 'PARE':
    if sexo == 'H' or sexo == 'M':
        print('Ok, obrigado.')
        sexo = 'PARE'
    else:
        sexo = str(input('Invalido, por favor digite seu sexo: ')).upper()
#while sexo not in