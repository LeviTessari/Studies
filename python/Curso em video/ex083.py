n = []
a = str(input('Digite uma expressão: '))
n.append(a)
b = a.count('(')
c = a.count(')')
if b == c:
    print('Expressão esta correta!')
else:
    print('Expressão esta errada!')