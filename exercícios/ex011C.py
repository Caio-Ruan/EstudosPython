print('======SALÁRIO======')
n = str(input('Colaborador: '))
p = int(input('Meta de vendas: '))
i = int(input('Vendas este mês: '))
m = float(input('Salário: '))


a = m * 0.15   #Cálculo para saber 15% do valor
b = m + a      #  //     //  Adicionar 15% ao salário
c = m - a      #  //     //  Subtrair 15% do    //
d = m * 0.10   #  //     //  saber 10% do   //
f = m + d      #  //     //  Adicionar 10% ao   //
e = m - d      #  //     //  Subtrair 10% do  //

if i == p:
    print(f'Parabéns! Meta atinginda!!\nSalário: R${m}')
if i < p:
    print(f'Não atingiu a meta\n Salário descontado 5% (R${a}) por não atingir meta: R${c}')
if i > p:
    print(f'Parabéns!! Superou a meta!\nO colaborador {n} foi muito prestativo este mês e obteve um bônus salarial de 15% (R${a:.2f})\nSalário: R${b}')
