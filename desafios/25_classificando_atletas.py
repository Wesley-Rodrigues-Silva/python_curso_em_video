from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação MIRIM')
elif idade >= 10 and idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classificação INFANTIL')
elif idade >= 15 and idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação JÚNIOR')
elif idade >= 20 and idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.')
    print('Classificação MASTER')



