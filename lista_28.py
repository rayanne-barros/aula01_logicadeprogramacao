A = int(input("Informe o valor de A: "))
B = int(input("Informe o valor de B: "))
C = int(input("Informe o valor de C: "))

x1 = (- B + (B**2 - (4 * A * C))**(1/2)) / (2 * A)
x2 = (- B - (B**2 - (4 * A * C))**(1/2)) / (2 * A)

print(x1)
print(x2)
