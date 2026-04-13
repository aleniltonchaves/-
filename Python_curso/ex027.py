#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
nome = str(input('Informe o nome completo: ')).strip()
n = nome.split()
print('Analizando...')
print(f'O primeiro nome é: {n [0]}')
print (f'O Sobrenome é: {n[len(n)-1]} ')
