print('======Média do Período======')
a = str(input('Nome do Aluno: '))
b = input('Cadeira: ')
n = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

m = (n+n2)/2

print(f'A Média de {a} é: {m}')
if m >= 7:
    print('Discente Aprovado')
else:
    print('Discente em recuperação')
