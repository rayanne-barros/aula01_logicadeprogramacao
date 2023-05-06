valor = float(input("Digite o valor do produto: "))
porcentagem = int(input("Digite a porcentagem do desconto: "))
porcentagem_real = (float) (porcentagem/100)
valor_do_desconto = valor * porcentagem_real
valor_final = valor - valor_do_desconto
print(valor_final)

