# Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada;
# calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operação aritmética escolhida.
# Símbolo Operação aritmética
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potenciação

operacao = input('+ -> Adicção \n - -> Subtracão'
                 ' \n * -> Multiplicação \n / -> Divisão \n ** -> Potenciação '
                 '\n Qual operação deseja resolver? ')

num1 = float(input('Digite o valor do número 1: '))
num2 = float(input('Digite o valor do número 2: '))

if operacao == '+':
    print(f'O valor da soma é: {num1 + num2}')
elif operacao == '-' and num1 >= num2:
    print(f'O valor da subtração é: {num1 - num2}')
elif operacao == '-' and num2 >= num1:
    print(f'O valor da subtração é: {num2 - num1}')
elif operacao == '*':
    print(f'O valor da multiplicação é: {num2 * num1}')
elif operacao == '/' and num1 >= num2:
    print(f'O valor da divisão é: {num1 / num2}')
elif operacao == '/' and num2 >= num1:
    print(f'O valor da divisão é: {num2/ num1}')
elif operacao == '**':
    print(f'A base é {num1} e o expoente é o {num2} ')
    print(f'O valor da subtração é: {num1 ** num2}')
