#Contar quantas vogais há em uma frase.

print("Olá! O programa irá solicitar uma frase/texto e verificar quantas vogais há.\n")

vogal_a = 0
vogal_e = 0
vogal_i = 0
vogal_o = 0
vogal_u = 0

frase = str(input("Digite a frase: "))

for letra in frase.lower(): #Deixar todas as letras minúsculas.
    if letra == 'a':
        vogal_a += 1

    elif letra == 'e':
        vogal_e += 1

    elif letra == 'i':
        vogal_i += 1

    elif letra == 'o':
        vogal_o += 1

    elif letra == 'u':
        vogal_u += 1

print(f"Nessa frase há:\n'A' - {vogal_a}\n'E' - {vogal_e}\n'I' - {vogal_i}\n'O' - {vogal_o}\n'U' - {vogal_u}")