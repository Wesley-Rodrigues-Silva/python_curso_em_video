import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

resul_co = co ** 2
resul_ca = ca ** 2
soma = resul_co + resul_ca
hipo = math.sqrt(soma)    

print(f'A hipotenusa vai medir {hipo:.2f}')
