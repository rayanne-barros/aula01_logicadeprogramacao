#Desenvolva um programa para calcular a venda de maçãs em uma banca de feira.
#O cliente compra maçãs custando R $1,37 cada uma,
#mas caso ele compre a partir de uma dúzia pagará com desconto de 10%,
#portanto o valor da unidade ficará por R $1,24.
#O programa deverá receber o número de maçãs desejadas pelo cliente, e retornar o valor total da compra.

quantidade_maca = int(input('Digite a quantidade de maças que deseja comprar: '))
if(quantidade_maca > 11):
    preco_unitario = 1.24
    valor_compra = quantidade_maca * preco_unitario
    print(f'O valor da sua compra é {valor_compra}')
else:
    preco_unitario = 1.3713
    valor_compra = quantidade_maca * preco_unitario
    print(f'O valor da sua compra é {valor_compra}')


