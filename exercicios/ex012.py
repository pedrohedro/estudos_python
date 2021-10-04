#faça um algoritimo que leia o preço de um produto e mostre seu novo preço
#com 5% de desconto.

p = float(input('Digite o valor da sua compra!: '))
d = p*0.05
print('olha só voce teve um desconto de 5% equivalente a {},logo você pagará um total de {}, olha só que maravilha!!! '.format(d, (d-p)))