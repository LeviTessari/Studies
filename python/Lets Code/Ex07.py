# Questão 7.
# Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
# coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
# segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
# euclidiana entre os pontos, utilizando a equação abaixo:
# 𝑑 = (𝑥2 − 𝑥1)² + (𝑦2 − 𝑦1)²
from math import sqrt

pontos = [[], []]


def distancia(x1, y1, x2, y2):
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d


print('Bem vindo ao programa do cálculo da distância entre dois pontos')
for i in (0, 1):
    pontos[i].append(int(input(f'Digite o valor para x{i}: ')))
    pontos[i].append(int(input(f'Digite o valor para y{i}: ')))
print(f'Os pontos escolhidos foram: {pontos} e a distância entre eles é de {distancia(pontos[0][0], pontos[0][1], pontos[1][0], pontos[1][1]):.2}')
