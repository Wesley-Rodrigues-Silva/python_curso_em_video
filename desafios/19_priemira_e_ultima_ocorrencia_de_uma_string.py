frase = str(input('Digite uma frase: ')).strip().upper()
letra = 'A'
print(f'A letra A aparece {frase.count(letra)} na frase.')
print(frase.find('A')+1)
print(frase.rfind('A')+1)