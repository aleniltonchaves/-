#Faça um programa que leia 3 números e mostre qual é o maior e qual o menor entre eles.
a = float(input('Digite um número: '))
b =  float(input('Digite outro número: '))
c =  float(input('Digite mais um número: '))
# maneira de verificar o menor número...
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'o menor número digitado foi: {menor}.')
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f' O maior número digitado foi: {maior}.')