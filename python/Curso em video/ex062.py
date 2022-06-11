termo1 = int(input("digite o primeiro termo: "))
razão = int(input('Digite a razão: '))
i=1
t = 10
print('{} termo vale {}.'.format(1, termo1))

while i != 0:
    i += 1
    final = termo1 + razão*i
    print('{} termo vale {}.'.format(i, final))
    if i == t: #quando ele chegar no if ele sempre vai parar, a função do programa é que ele SEMPRE PARE AQUI
        n = int(input('Quantos termos você quer ve agora?'))
        if n != 0:
            t = t + n #através disso vc força ele sempre parar 
        else:
            i = 0