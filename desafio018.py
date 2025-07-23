from math import cos, tan, sin, radians

ang= float(input('Digite o ângulo desejado: '))

# rad = radians(ang)
seno = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))

print('Para o ângulo {:.2f}, o seno foi de {:.2f}.'.format(ang, seno))
print('Para o ângulo {:.2f}, o cosseno foi de {:.2f}.'.format(ang, cose))
print('Para o ângulo {:.2f}, a tangente foi de {:.2f}.'.format(ang, tang))