#Um programa é necessário para habilitar o funcionamento de uma conta corrente em um banco digital.
# O programa deve permitir ao cliente iniciar com um depósito, realizar um saque,
# e ao final verificar se o saldo da conta está positivo ou negativo.
# Se negativo, informa qual o valor será necessário para quitar o débito.

saldo= 0
deposito = float(input('Qual valor deseja depositar? '))
saldo +=deposito
saque = float(input('Qual valor deseja sacar? '))
saldo-=saque
if(saque > saldo):
    print(f"Sua conta está negativada você deverá pagar {-saldo} reais")


