#Crie um programa que leia um número Real qualquer pelo teclado mostre na tela a sua porção inteira.
from math import trunc

n = float(input('Digite um número:'))
print('O valor digitado foi {} e a parte inteira é {}.'.format(n, trunc(n)))