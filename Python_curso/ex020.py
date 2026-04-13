#O mesmo professor do desafio anteriro quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = str(input('Informe o nome do aluno 1 candidato a apresentar o trabalho: '))
aluno2 = str(input('Informe o nome do aluno 2 candidato a apresentar o trabalho: '))
aluno3 = str(input('Informe o nome do aluno 3 candidato a apresentar o trabalho: '))
aluno4 = str(input('Informe o nome do aluno 4 candidato a apresentar o trabalho: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(lista)