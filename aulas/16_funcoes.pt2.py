'''def somar (a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,5)'''

'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''

'''def somar(a=0, b=0, c=0):
    s = a + b +c
    return s
r1 = somar(3, 2, 5)
r2 = somar(2,2 )
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')
        