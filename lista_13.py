

quantidade_maxima = float(input('Qual a quantidade máxima de calça para o estoque? '))
quantidade_minima = float(input('Qual a quantidade mínima de calça para o estoque? '))
quantidade_real = float(input('Qual a quantidade real do estoque?'))

media = (quantidade_maxima + quantidade_minima) / 2


if quantidade_real < media:
    print('Você precisa comprar mais calças!')
elif quantidade_real > media:
    print('Você não precisa comprar mais calças!')
elif quantidade_real == media:
    print('Em breve você precisará comprar mais calças!')



