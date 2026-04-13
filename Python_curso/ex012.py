#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p1 = float(input('Digite o preço do produto: '))
p2 = p1 - 0.05 * p1
print('O valor do produto, com 5% de desconto, agora é de R${:.2f} reais'.format(p2))