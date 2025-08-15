from random import randint
from time import sleep

print('=-'* 20)
print('Vou penar em um número entre 0 e 5. Tente adivinhar...')
print('=-'* 20)

num = int(input('Digite um número de 0 a 5: '))
sort= randint(0, 5)
print('PROCESSANDO...')
sleep(3)

if num == sort:
    print('Parabéns vc acertou o número.') 
else:
    print('Vc errou o número, pensei no número {}.'.format(sort))

