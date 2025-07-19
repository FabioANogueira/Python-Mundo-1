#nome = str(input('Qual é o seu nome? '))
#print('Prazer em te conhecer {:=^20}'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
rest = n1%n2
ex = n1**n2
media = (s)/2
print('A soma vale {}, \n o produto vale {} \n e a divisao {:.3f}'.format(s, m, d))
print('A divisão inteira {}, o resto {}.'.format(di, rest), end='+++ ')
print('A média entre {} e {} é {}.'.format(n1,n2,media))

