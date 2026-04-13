from turtledemo.chaos import f
from typing import Type


def analisar_entrada():
    entrada = input(' Digite algo: ')


# Verificar o tipo primitivo
tipo_primitivo = type(entrada)
analisar_entrada()
#informações sobre a entrada
print(f'Tipo primitivo: {tipo_primitivo._name_}')
print(f'É um número? {entrada.isnumeric()}')
print(f'É alfabético? {entrada.isalpha()}')
print(f'É alfanumérico? {entrada.isalnum()}')
print(f'É composto APENAS por espaços? {entrada.isspace()}')
print(f'É um título? {entrada.istitle()}')
print(f'Está em letra maiúsculas? {entrada.isupper()}')
print(f'está em letras minúsculas? {entrada.islower()}')

analisar_entrada()
#Tentar converter para outros tipos
try:
    int_entrada = int(entrada)
    print(f'Valor inteiro:{int_entrada}')
except ValueError:
    pass
try:
    float_entrada = float(entrada)
    print(f'Valor floar:{float_entrada}')
except ValueError:
    pass
analisar_entrada()