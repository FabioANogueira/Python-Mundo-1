from math import sqrt, hypot

cat_oposto = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digiteo cateo adjacente: '))

#hipotenusa = ((cat_oposto**2 + cat_adj**2) * 0.5)
#hipotenusa = sqrt(cat_oposto**2 + cat_adj**2)
hipotenusa = hypot(cat_oposto, cat_adj)

print('O cateto oposto é {} e o ' \
'cateto adjacente é {}, resultando hipotenusa {:.2f}.'.format(cat_oposto, cat_adj, hipotenusa))