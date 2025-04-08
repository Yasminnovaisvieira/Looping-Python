#Entre 10 números quais são pares e quais são ímpares.

print("Olá! O programa irá solicitar 10 números e verificar quais são pares e quais são ímpares.\n")

pares = []
impares = []

for i in range(1,11):
    numero = int(input(f"Digite o {i}º número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\nOs números ímpares são: {impares}")
print(f"Os números pares são: {pares}")