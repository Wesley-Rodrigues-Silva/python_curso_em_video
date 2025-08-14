from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
ano_alistamento = ano_nasc + 18
if idade < 18:
    faltam = 18 - idade
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
    print(f'Ainda faltam {faltam} ano para o alistamento')
    print(f'Seu alistamento será em {ano_alistamento}')
elif idade == 18:
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
    print(f'Seu alistamento é este ano, você deve se alistar IMEDIATAMENTE!')
else:
    tempo = idade - 18
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')
    print(f'Você já deveria ter se alistado há {tempo} anos atrás')
    print(f'Seu alistamento foi em {ano_alistamento}')