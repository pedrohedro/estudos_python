# nome = input('Qual é o seu nome?')
# print ('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d= n1 / n2
di = n1 // n2
e = n1 ** n2 
print ('A soma vale {}, \n o produto é {} \n e a divisão é {:.3}'.format(s, m, d))
print(' A divisão inteira é {} \n e potencia {}'.format(di, e))