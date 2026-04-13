#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
n = float(input('Digite um valor em metros: '))
c = 100 * n
m = 1000 * n
print('O valor de {} metros é equivalente a {} centimetros e a {} milimetros'.format(n, c, m))
