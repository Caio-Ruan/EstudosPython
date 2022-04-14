print('======Desconto======')
n = float(input("Qual o preço do produto?: "))

a = n * 0.05
b = n - a

print(f'O produto terá desconto á vista de 5% (R${a:.2f})\nValor a pagar (á vista): R${b:.2f}')
