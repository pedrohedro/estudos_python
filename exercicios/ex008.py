#escreva um programa que leia um valor em metros 
# e o exiba em centimetros e milimetros
n=int(input('Escreva uma quantidade em metros: '))
print('o valor de {} metros vale {}cm  \n{} mm \n{}Km'.format(n, (n*100), (n*1000), (n/1000)))