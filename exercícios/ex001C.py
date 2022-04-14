print('====== Exercício 04 ======')
n = input('Digite algo: ')
print(f'O tipo primitivo do que foi escrito é: {type(n)}'), \
print(f'É um número?  {n.isnumeric()}'),
print(f'É decimal? {n.isdecimal()}'),
print(f'É um digito? {n.isdigit()}'),
print(f' é ..{n.isidentifier()}'),
print(f'Está em caps? {n.isupper()}'),
print(f'está em minúsculo? {n.islower()}')
