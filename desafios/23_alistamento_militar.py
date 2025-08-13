from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_atual
ano_alistamento = ano_nasc + 18
if ano_alistamento < 18:
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
    print(f'')
    print(f'Seu alistamento será em {ano_alistamento}')
elif ano_alistamento == 18:
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
    print(f'Seu alistamento é este ano, você deve se alistas IMEDIATAMENTE!')
else:
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
    print(f'Seu alistamento será em {ano_alistamento}')