#Cores no terminal - Para adcionar a cor no terminal, padão ANSI, deve seguir a estrutura:
# \033[0;33:34m - codigo para style (0:4), text(30:37), back (40:47)
#import pandas as pd
#cor_no_terminal = [
  #  {'codigo_0' : 0 , 'style' : 'none'}, {'codigo_0': 1, 'style': 'bold'}, {'codigo_0' : 2, 'style' : 'bold' }, {'codigo_0' : 3, 'style' : 'underline'}, {'codigo_0': 4,'style': 'negative'},
    #{'codigo_1' : 30, 'style' : 'branco'}, {'codigo_1' : 31, 'style' : 'vermelho'}, {'codigo_1' : 32, 'style': 'verde'}, {'codigo_1': 33, 'stylo': 'amarelo'},
    #{'codigo_1': 34, 'stylo' :'azul'},{'codigo_1' : 35, 'stylo': 'roxo'}, {'codigo_1' : 36, 'stylo': 'azul claro'}, {'codigo_1': 37, 'stylo': 'cinza'},
    #{'codigo_2' : 40, 'style' : 'branco'}, {'codigo_2' : 41, 'style' : 'vermelho'}, {'codigo_2' : 42, 'stylo' : 'verde'}, {'codigo_2' : 43, 'style' : 'amarelo'},
   # {'codigo_2' : 44, 'stylo' : 'azul'}, {'codigo_2' : 45, 'stylo' : 'roxo'},{'codigo_2' : 46, 'stylo' : 'azul claro'}, {'codigo_2' : 47, 'stylo' : 'cinza'},
 #]
#
#tabela_pandas = pd.DataFrame (cor_no_terminal)
#print (tabela_pandas)


#Cores no terminal - Para adcionar a cor no terminal, padão ANSI, deve seguir a estrutura:
# \033[0;33:34m - codigo para style (0:4), text(30:37), back (40:47)
import pandas as pd
cor_no_terminal = [
    {'codigo' : '---definir o' , 'style' : 'estilo_de_texto ---'},
     {'codigo' : 0 , 'style' : 'none'}, {'codigo': 1, 'style': 'bold'}, {'codigo' : 4, 'style' : 'underline'}, {'codigo': 7,'style': 'negative'},
    {'codigo' : '---def_cor', 'style' : 'do_texto---'},
    {'codigo' : 30, 'style' : 'branco'}, {'codigo' : 31, 'style' : 'vermelho'}, {'codigo' : 32, 'style': 'verde'}, {'codigo': 33, 'style': 'amarelo'},
    {'codigo': 34, 'style' :'azul'},{'codigo' : 35, 'style': 'roxo'}, {'codigo' : 36, 'style': 'azul claro'}, {'codigo': 37, 'style': 'cinza'},
     {'codigo' : '---def_cor', 'style' : 'de_fundo---'},
    {'codigo' : 40, 'style' : 'branco'}, {'codigo' : 41, 'style' : 'vermelho'}, {'codigo' : 42, 'style' : 'verde'}, {'codigo' : 43, 'style' : 'amarelo'},
    {'codigo' : 44, 'style' : 'azul'}, {'codigo' : 45, 'style' : 'roxo'},{'codigo' : 46, 'style' : 'azul claro'}, {'codigo' : 47, 'style' : 'cinza'},
 ]

#dicionário de cores - -
nome = 'Alenilton'
cores = {' limpa' : '\033[m' ,
               'azul' : '\033[34m' ,
               'Amarelo': '\033[33m',
               'pretoebranco' : '\033[7:30m' }

print(f'Olá, {cores},{nome}, prazer em te conhecer!')



tabela_pandas = pd.DataFrame (cor_no_terminal)
print (tabela_pandas)