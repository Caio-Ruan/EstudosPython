from math import hypot
n1 = float(input('Valor Cateto Oposto: '))
n2 = float(input('Valor Cateto Adjacente: '))

# num1 = n1 ** 2
# num2 = n2 ** 2
# c = (num1 + num2) ** (1/2)
# é o normal, porém com ''import math'' resolvemos assim:

hi = hypot(n1, n2)

print(f'{n1:.0f}² + {n2:.0f}² = {hi:.2f}')
