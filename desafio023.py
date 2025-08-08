num = int(input('Digite um número de 0 a 9999: '))
n = str(num).zfill(4)  # Preenche com zeros à esquerda se necessário
print('O número digitado foi: {}'.format(num))
print('Milhar: {}'.format (n[0]))
print('Centena: {}'.format(n[1]))
print('Dezena: {}'.format(n[2]))      
print('Unidade: {}'.format(n[3]))

