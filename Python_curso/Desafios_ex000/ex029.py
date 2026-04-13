# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
# mostre uma mensagem deizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
v = int(input(' Informe a velocidade atual do veículo: ' ))
m = (v-80)*7
if v > 80:
    print(f'Você foi multado em R$ {m},00 reais')
else:
    print( 'Dentro do limite permitido. '
           'Você não foi multado!' )
