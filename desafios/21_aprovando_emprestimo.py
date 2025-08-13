valor_casa = int(input('Valor da casa: R$ '))
salario = int(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor_casa / (anos * 12)
print(f'Para pagar uma casa de R${valor_casa} em {anos} anos a prestação será de R${prestacao:.2f}')
if prestacao >= salario * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Emprestimo ACEITO')