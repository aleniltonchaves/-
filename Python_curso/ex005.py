# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input(' Digite um número: '))
antecessor = n1 - 1
sucessor = n1 + 1
print(' Seu antecessor é {}, e seu sucessor é {}.' .format(antecessor, sucessor))