from math import sqrt, hypot

cat_oposto = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digiteo cateo adjacente: '))

hipotenusa = sqrt(cat_oposto**2 + cat_adj**2)

print('O cateto oposto é {} e o ' \
'cateto adjacente é {}, resultando hipotenusa {}.'.format(cat_oposto, cat_adj, hipotenusa))