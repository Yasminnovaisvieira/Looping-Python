#Verifica quantos números são abaixo da média.

print("Olá! O programa irá verificar a média dos números digitados e quantos estão abaixo dela.\n")

quantidade = int(input("Quantos números você deseja digitar? "))

soma = 0
numeros = []
i = 0

while i < quantidade:
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    soma += num
    i += 1

media = soma / quantidade

menores = 0
y = 0

while y < quantidade:
    if numeros[y] < media:
        menores += 1
    y += 1

print(f"\nA média é: {media}")
print(f"Quantidade de números menores que a média: {menores}")
