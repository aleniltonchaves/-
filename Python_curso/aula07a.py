#aula sobre os operadores básicos aritiméticos
#Ordem de procedência -> primeiro () ; segundo **; terceiro *,/,//,% ; quarto +,-;

#nome = input(' Qual é seu nome? ')
#print('Prazer em te conhecer {:-^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2  = int( input('Digite outro valor: '))
s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
su = n1-n2
e = n1**n2
print('A soma vale {}, o produto é {}, a divisão é {:.2f}, a divisão inteira é {}, a subtração é {}, e a exponenciação é {}.'.format(s,m, d, di, su, e))