#crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
r = float(input('Digite o valor, em reais, que você têm na carteira:R$ '))
d = float(input('Na cotação atual, 1 Dollar vale quantos reias? Informe:R$ '))
c = r / d
print('É possível adquirir $$ {:.2f} dollares com R${:.2f} reais'.format(c,r))