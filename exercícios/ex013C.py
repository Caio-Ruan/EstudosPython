print('======Alugue um carro======')
n = int(input('Quantos dias alugados? '))
a = float(input('Quantos Km rodados? '))

b = n * 60
c = a * 0.15
t = c + b

print(f'Você alugou com a diária de  R$60 por {n} dias (R${b})\nVocê alugou com a taxa de R$0.15 o Km e percorreu {a}Km (R${c})')
print(f'======Total a pagar: R${t}======')
