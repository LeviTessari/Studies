#Meu jeito
city = str(input('Em que cidade você nasceu? '))

city1 = city.upper()
vdd = 'SANTO' in city1
print('{}'.format(vdd))

#Professor
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO') #Tirar espaço, jogar pra maiusculo para nao ter erro e igualar