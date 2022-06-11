i = 0
fibo = []
f1 = 0
f2 = 1
fibo.append(f1)
fibo.append(f2)
n = int(input('Qual número da sequência de Fibo vc qr ver? '))
while i < n-2:
    i+= 1
    F = f1 + f2
    fibo.append(F)
    f1 = f2
    f2 = F
print(fibo)