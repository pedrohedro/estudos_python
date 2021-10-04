#faça um programa que leia a largura e a altura de uma parede em metros,
#  calcule a sua área e a qauntidade de tinta necesária para pinta-la,
#sabendo que cada litro pinta uma area de 2m2

l=float(input('Digite a largura da parede: '))
h=float(input('Digite a altura da parede:  '))
A= h*l
print('a area da parede é {}m'.format(A))
print ('a quantidade de tinta necessária é de {}'.format((A/2)))