n1 = float(input('Digite a primeira nota: ')) 
n2 = float(input('Digite a segunda nota: '))
m = n1+n2/2
print(f'sua media foi {m}.')
if m >= 6.0:
    print('Voce está na média!')
else:
    print(f'Você não foi bem, estude mais!')