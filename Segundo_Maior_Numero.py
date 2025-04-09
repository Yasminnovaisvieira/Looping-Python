#Encontrar segundo maior número.

print("Olá! O programa irá verificar qual é o segundo maior valor declarado.\n")

quantidade = int(input("Quantos números você deseja digitar? "))

maior = int(input("Digite um número: "))
segundo = maior

for i in range(quantidade - 1):
    numero = int(input("Digite um número: "))

    if numero > maior:
        segundo = maior
        maior = numero

    elif numero > segundo and numero != maior:
        segundo = numero

if segundo == maior:
    print("\nNão existe segundo maior número.")
else:
    print(f"\nO segundo maior número é: {segundo}")