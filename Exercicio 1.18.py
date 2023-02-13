#Faça um programa que peça o tamanho de um arquivo para download 
# (em MB) e a velocidade de um link de Internet (em Mbps), calcule e 
# informe o tempo aproximado de download do arquivo usando este link 
# (em minutos).


print('Bem vindo!!')

tamanho_arquivo = float(input('Insira o tamanho do arquivo:'))
velocidade_link = 90

print('O tempo de download é: ', (tamanho_arquivo/velocidade_link)*60)