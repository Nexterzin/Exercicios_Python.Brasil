#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando 
# as seguintes fórmulas:
#A - Para homens: (72.7*h) - 58
#B - Para mulheres: (62.1*h) - 44.7

print('Bem vindo!!')

genero = input('Informe seu genero H/M: \n')

if genero == 'H':
    alturah = float(input('Informe sua altura: '))
    pesoh = (72.7*alturah) - 58
    print('Seu peso ideal é: ', pesoh)
elif genero == 'M':
    alturam = float(input('Informe sua altura: '))
    pesom = (62.1*alturam) - 44.7
    print('Seu peso ideal é: ', pesom)
else:
    print('Erro!!')