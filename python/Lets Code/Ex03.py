#Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
#área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
#💡 Dica: Para utilizar um valor mais preciso do pi (ℼ), você pode importar a biblioteca math, e
#utilizar o math.pi, como ilustrado no código abaixo:
#import math
#print(math.pi)

from math import pi
raio = float(input('Digite valor do raio que você deseja calcular: '))
print(f'O valor de raio {raio}\n'
      f'Perimetro da circunferência é {2*pi*raio:.2f}\n'
      f'Área é {pi*(raio**2):.2f}')
