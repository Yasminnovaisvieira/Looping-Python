# Solicitar 10 números, usando for, e verificar quantos são múltiplos de 3.

print("Olá! O programa irá solicitar 10 números e verificar quantos são múltplos de 3.\n")

quantidade = 0

for numero in range(1, 11):
    numero = int(input(f"Digite o {numero}º número: "))

    if numero % 3 == 0:
        quantidade = quantidade + 1

print(f"\nA quantidade de números múltiplos de 3: {quantidade}")