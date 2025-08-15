
vel = float(input('Digite a velocidade do carro: ' ))
multa = float((vel - 80) * 7)
if vel > 80:
    print('A velocidade está acima do limite {}.'.format(vel))
    print('Você pagará multa de R$ {:.2f}.'.format(multa))
else:
    print('Parabéns vc estava na velocidade correta')

