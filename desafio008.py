metros = float(input('Digite um valor em metros: '))

cent = metros * 100
mili = metros * 1000

print('Foram digitados {:.2f} metros, sendo {:.2f} centimetros e {:.2f} milimetros.'.format(metros, cent, mili))
