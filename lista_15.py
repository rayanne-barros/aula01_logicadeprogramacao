
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em Kg: '))

imc = (peso / altura**2)

if imc < 18.5:
    print(f"Seu índice de massa corpórea é de {imc:.2f}, classificado como abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print(f"Seu índice de massa corpórea é de {imc:.2f}, classificado como normal")
elif 25 <= imc <= 30:
    print(f"Seu índice de massa corpórea é de {imc:.2f}, classificado como sobrepeso")
elif imc > 30:
    print(f"Seu índice de massa corpórea é de {imc:.2f}, classificado como obesidade")
