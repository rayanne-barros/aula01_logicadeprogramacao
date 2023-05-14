# Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando divididos por 11,
# produzam o resto igual a 5.

minimo = 1000
maximo = 2000

for num in range(minimo, maximo):
    if num % 11 == 5:
        print(num)


