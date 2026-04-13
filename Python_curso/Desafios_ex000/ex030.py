# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
n = int (input(' Digite um número inteiro: '))
rest = n % 2  #o resto será sempre 0 ou 1, assim definimos a condição;
if rest == 0 :
    print(f'O número {n} é par, pois ele termina em 0, 2, 4, 6 ou em  8. ')
else:
        print(f'O número {n} é ímpar pois não termina em 0, 2, 4, 6 ou 8. ')
