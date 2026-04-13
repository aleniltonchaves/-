#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcula o preço a pagar, sabendo que
# o carro custa R$60 por dia e R$0,15 por km rodado.
k1 = float(input('Informe a quilometragem inicial do veiculo: '))
k2 = float(input('Informe a quilometragem final do veiculo: '))
k = k2 - k1
d = float(input('Informe a quantidade de dia pelos quais o veiculo ficou alugado: '))
total_dias = 60 * d
total_km = k * 0.15
t = total_km + total_dias
print('O custo do aluguel no período de {} dias é de R${}, considerando que o veiculo percorreu {}km.'.format(d, t
                                                                                                              , k ))