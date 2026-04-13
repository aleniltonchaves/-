#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salário superior a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
s = float(input(f'Informe seu salário atual: '))
if s<= 1250:
    aumento = s + (s *15 / 100)
else:
    aumento =  s + (s * 10/100)
print(f' Se você ganhava R$ {s:.2f}, agora ganhará R$ {aumento}.')
