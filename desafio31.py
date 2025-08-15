dist = float(input('Digite a distância da viagem em KM: '))

if dist <= 200:
    preco = dist * 0.50

else:
    preco= dist * 0.45
print('A viagem terá {} km de distância e custará {:.2f} reais.'.format(dist, preco))



