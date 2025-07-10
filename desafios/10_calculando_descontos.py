n = float(input('Qual é o preço do produto? R$'))
d = n * (5/100)
desconto = n - d
print(f'O produto que custava {n}, na promoção com desconto de 5% vai custar R${desconto:.2f}')