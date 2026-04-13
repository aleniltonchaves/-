#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta a área de 2m².
l = float(input('Digite a largura da parede, em metros: '))
a = float(input('Digite a atura da parede, em metros: '))
m = a * l
li = m / 2
print('A parede tem {:.2f}m² e será nescessário {:.2f} litros de tinta para pintá-la.'.format(m,li))