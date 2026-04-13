#Faça um programa que leaia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite o valor do ângulo: '))
sin = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)
print('O Seno de {} vale {:.2}, o cosseno de {} vale {:.2} e a tangente de {} vale {:.2}.'.format(a, sin, a, cos, a, tan))