fatorial = int(input('Digite um valor: '))
multiplicador = 1
print('{} ! = {}'.format(fatorial, fatorial),  end=' x ')
while fatorial != 1:
   multiplicador = multiplicador*fatorial
   fatorial -= 1
   print('{}'.format(fatorial), end=' x ')


print('= {}'.format(multiplicador))