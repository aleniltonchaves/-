#Desenvolva um programa que leia as duas notas de um aluno, calcula e mostra sua média.
n1 = float(input('Digite a nota primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2)/2
print('A média entre as notas {}, e {}, é {}.'.format(n1, n2, m))