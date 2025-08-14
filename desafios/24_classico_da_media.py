import math
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = math.ceil(((n1 + n2) / 2) * 10) / 10
if media >= 7.0:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media:.1f}')
    print('O aluno está APROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media:.1f}')
    print('O aluno está de RECUPERAÇÃO!')
else:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media:.1f}')
    print('O aluno está de REPROVADO!')