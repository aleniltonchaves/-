#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from time import sleep
from random import randint
num = randint (0, 5) # Sorteador
print('-=-' *46)
print ('-=--=-Escolhi um número entre 0 e 5. '
       'Se você adivinhar qual foi o número escolhido por mim, '
       'você será o ganhador!-=---=-')
print('-=-' *46)
n = int( input( 'Informe seu palpite: '))
print ('processando...')
sleep(3)
if n == num :
    print ( f'Sim, eu escolhi {num} .Você ganhou!')
else:
    print(f'Eu pensei em {num}. Voce perdeu!')
print( f' Tente outra vez!')
