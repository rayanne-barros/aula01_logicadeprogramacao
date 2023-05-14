maior = 0
menor = 0
for a in range(1, 16):
    altura = float(input('Altura da {}° pessoa: '.format(a)))
    if a == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
print('A maior altura foi de {}metros'.format(maior))
print('A menor altura foi de {}metros'.format(menor))

