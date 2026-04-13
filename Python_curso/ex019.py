#Um professor querr sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
#que ajude ele, lendo o nome dos alunos e escrevendo  o nome escolhido.
import math
import random

aluno1 = str(input('Informe o nome do aluno 1 candidato a limpar o quadro: '))
aluno2 = str(input('Informe o nome do aluno 2 candidato a limpar o quadro: '))
aluno3 = str(input('Informe o nome do aluno 3 candidato a limpar o quadro: '))
aluno4 = str(input('Informe o nome do aluno 4 candidato a limpar o quadro: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('O aluno escolhido foi: {}'.format(sorteio))