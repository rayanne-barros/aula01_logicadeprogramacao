# Escrever um algoritmo que escreve os números ímpares entre 100 e 200.

maximo = 200
contador = 100

while contador < maximo:
    contador += 1
    if contador % 2 == 1:
        print(contador)

