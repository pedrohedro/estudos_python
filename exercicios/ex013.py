#faça um algoritimo que leia o preço de um produto e mostre seu novo preço
#com 5% de desconto.

p = float(input('Digite o valor do seu salário!: '))
d = p*0.15
print('Olha só voce teve um aumento de {} reais equivalente a 15% do seu salário,logo você ganhará um total de {}, olha só que maravilha!!! '.format(d, (d+p)))