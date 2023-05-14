#  Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos
#  de três e que se encontram no conjunto dos números de 1 até 500


maximo = 500

contador = 0
soma = 0
numeros_impares_multiplos_de_3 = 0
while contador < maximo:
    contador += 1
    if contador % 2 == 1:
        if contador % 3 == 0:
            print(contador)
            soma += contador
            numeros_impares_multiplos_de_3 += 1

print(f'{numeros_impares_multiplos_de_3} numeros foram somados e o resultado dessa soma é de {soma}')