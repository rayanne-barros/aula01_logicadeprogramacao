# Faça um algoritmo para calcular o volume de uma esfera de raio R, em que R é um dado
# fornecido pelo usuário. O volume da esfera é dado por 𝑉 = (4/3) * ℼ * 𝑅 **3



raio = float(input('Digite o raio de uma esfera: '))
PI = 3.15
volume = (4/3) * (PI * raio ** 3)
print('O volume da esfera é: %.2f' %volume)