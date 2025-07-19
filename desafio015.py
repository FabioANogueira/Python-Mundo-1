dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

preco_dias = dias * 60
preco_km = km * 0.15
total = preco_dias + preco_km

print('O valor por dia foi de R$ {:.2f}, já o valor por km foi R$ {:.2f}, ficando o total de R$ {:.2f}'.format(preco_dias, preco_km, total))

