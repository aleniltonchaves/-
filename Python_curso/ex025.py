#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.
nome = str(input('Digite seu nome: ')).strip()
print('Analizando...')
print(f'Em seu nome há o sobrenome Silva? '
      f'{"SILVA" in nome.upper()}')
