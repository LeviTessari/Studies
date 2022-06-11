#Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
#Dica: Use três variáveis:
#● um contador;
#● uma variável para soma;
#● e uma variável para os termos.
#Lembre-se de que 4! = 4 * *3 ** 2 * *1, que também é igual a 4 ** 3!.
numero = 5
def fatorial(numero):
    contador = 0
    produto = 1
    while (numero - contador) != 1:
        termo = (numero - contador)
        contador = contador + 1
        produto = produto*termo
    return produto
#def somatoria(numero):
soma = 0
for i in range(1, 1001):
    valor = 1/fatorial(i)
    soma = soma + valor
    print(f'O valor é {valor} e a soma é {soma}')