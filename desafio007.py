n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A primeira nota foi {},  a segunda nota foi {}, e sua média foi {}'.format(n1,n2,media))

if media >= 7:
    print('PARABÉNS VOCÊ FOI APROVADO')
else:
    print('FOI REPROVADO')

