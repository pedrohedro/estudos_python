#crie um programa que leia quanto dinheiro uma pesoa tem 
#e mostre quantos dolares ela pode comprar considere valor do dolar atual

c=float(input('qual o seu saldo em conta: '))
print('Com R${:.2f} você pode comprar U${:.2f} Dolares ou '.format(c,(c/5.4)))
print ('Com R${:.2f} voce pode ter tambem {} BTC e {} ETH'.format(c, (c/263000), (c/18242)))