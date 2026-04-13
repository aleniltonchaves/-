#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o salário atual do funcionário:R$ '))
r = float(input('Digite o reajuste do salário desejado:%'))
n = r/100
n1 = s*n+s
print('O novo salário do funcionário, com o reajuste de {}%, agora é de: R${:.2f} ''reais'.format(r,n1))

