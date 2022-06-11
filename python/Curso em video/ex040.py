not1 = float(input('Primeira nota: '))
not2 = float(input('Segunda nota: '))
med = (not2+not1)/2
print('{}'.format(med))
if med < 5:
    print('\033[31mREPROVADO\033[m')
elif 5 <= med < 7:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[32mAPROVADO\033[m')