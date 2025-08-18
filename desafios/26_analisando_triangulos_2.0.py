p1 = int(input('Primeiro segmento: '))
p2 = int(input('Segundo segmento: '))
p3 = int(input('Terceiro segmento: '))
if p1 + p2 > p3 and p1 + p3 > p2 and p2 + p3 > p1:   
    if p1 == p2 == p3:
        print(f' {p1}, {p2} e {p3} PODEM formar um triângulo Equilátero')
    elif p1 == p2 or p1 == p3 or p2 == p3:
        print(f' {p1}, {p2} e {p3} PODEM formar um triângulo Isósceles')
    else:
        print(f' {p1}, {p2} e {p3} PODEM formar um triângulo Escaleno')
else:   
    print('Não é possível formar um triângulo')