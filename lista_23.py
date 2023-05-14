numero_positivo = 0
numero_negativo = 0
soma_numeros = 0
#num = 0
soma = 0
i= 0
while i != 1:
     #print('Digite um número ou 0 para parar: ')
    num = int(input('Digite um numero ou 0 para parar o programa: '))
    if num == 0:  #para sair do while
        i = 1
    else:
        if num > 0:
            numero_positivo += 1
        else:
            numero_negativo += 1

    soma_numeros += num
    soma += 1

print(f'A média aritmética dos números lidos é: {soma_numeros/soma}')
print(f'A quantidade de valores positivos é: {numero_positivo}')
print(f'A quantidade de valores negativos é: {numero_negativo}')






