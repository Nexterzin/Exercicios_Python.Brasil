#Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que 
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em 
# galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os 
# respectivos preços em 3 situações:

#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja 
# menor. Acrescente 10% de folga e sempre arredonde os valores para 
#cima, isto é, considere latas cheias.


print('Bem vindo!!')

tamanho = float(input('Informe o tamanho da area a ser pintada: '))

litro = tamanho / 6
latas = litro / 18

if tamanho % 108 != 0:
    latas += 1
    preco = latas * 80

galao = litro / 3.6
if galao %3.16 != 0:
    galao += 1
    preco2 = galao * 25

mistura_lata = int(litro/18)
mistura_galao = int((litro - (mistura_lata*18)) / 3.6)

if litro - (mistura_lata*18) % 3.6 == 0:
    mistura_galao += 1

print('Apenas latas de 18 litros: %d' % latas, 'preço: %d', preco)
print('Apenas galões de 3.6 litros: %d' % galao, 'preço: %d', preco2)
print('Mistura: %d latas e %d galoes = %.2f' % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))