# Apenas 3 tentativas para acertar a senha.

print("Olá! O programa irá pedir 2 números e verificar quais são os números que existem entre eles.\n")

numero_inicial = int(input("Digite o número inicial: "))
numero_final = int(input("Digite o número final: "))

for numero in range(numero_inicial, numero_final + 1):
    if numero >= 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                break
        else:
            print(f"Esse número é primo: {numero}")