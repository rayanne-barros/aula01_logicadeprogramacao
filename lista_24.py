# Escrever um algoritmo que leia uma quantidade desconhecida de númerose conte quantos
# deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deve terminar quando for lido um número negativo.

numero_entre0e25 = 0
numero_entre26e50 = 0
numero_entre51e75 = 0
numero_entre76e100 = 0
soma_numeros = 0
soma = 0
parada = 0
while parada != 1:
    # print('Digite um número ou 0 para parar: ')
    num = int(input('Digite um numero ou 0 para parar o programa: '))
    if num < 0:  # para sair do while
        parada = 1
    else:
        if 0 <= num <= 25:
            numero_entre0e25 += 1
        elif 26 <= num <= 50:
            numero_entre26e50 += 1
        elif 51 <= num <= 75:
            numero_entre51e75 += 1
        elif 76 <= num <= 100:
            numero_entre76e100 += 1


print(f'A quantidade de números entre 0 e 25 é: {numero_entre0e25}')
print(f'A quantidade de números entre 26 e 50 é: {numero_entre26e50}')
print(f'A quantidade de números entre 51 e 55 é: {numero_entre51e75}')
print(f'A quantidade de números entre 56 e 100 é: {numero_entre76e100}')
