# Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e
# a média geral dos números lidos. O número que encerrará a leitura será zero.

quantidade_numeros_pares = 0
quantidade_numero_impares = 0
soma_numeros = 0
media_numeros_pares = 0
soma_numeros_pares = 0
num_par = 0
media = 0
soma = 0
parada = 0

while parada != 1:
    num = float(input('Digite um numero maior que zero ou 0 para parar o programa: '))
    if num == 0:  #para sair do while
        parada = 1
    else:
        if num % 2 == 0:
            quantidade_numeros_pares += 1
            soma_numeros_pares += num
        else:
            quantidade_numero_impares += 1

    soma_numeros += num
    soma += 1
    media_numeros_pares = soma_numeros_pares / quantidade_numeros_pares

print(f'A média dos números pares lidos é: {media_numeros_pares}')
print(f'A média dos números lidos é: {soma_numeros/(soma-1)}')
print(f'A quantidade de numeros pares é: {quantidade_numeros_pares}')
print(f'A quantidade de numeros ímpares é: {quantidade_numero_impares}')

