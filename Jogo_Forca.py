# Jogo da Forca.

import random

print("Olá! O programa irá rodar o Jogo da Forca.\n")

palavras = ["gato", "computador", "java", "python", "unha"]
palavra_secreta = random.choice(palavras)

letras_corretas = []
letras_incorretas = []
total_tentativas = 6

while total_tentativas > 0:
    exibicao = ""

    for letra in palavra_secreta:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "

    print(f"Palavra: {exibicao}")
    print(f"Letras erradas: {letras_incorretas}")
    print(f"\nTentativas restantes: {total_tentativas}\n")

    if "_" not in exibicao: #Se '_' não estiver mostrando na tela.
        print(f"\nParabéns! Você acertou a palavra: {palavra_secreta}")
        break

    elif total_tentativas == 0:
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")

    print("---------------------------------------")
    chute = input("Digite uma letra: ").lower()

    if chute in letras_corretas or chute in letras_incorretas:
        print("\nVocê já tentou essa letra. Tente outra.")
        continue

    if chute in palavra_secreta and not chute == "":
        letras_corretas.append(chute)
        print("\nLetra correta!")
    else:
        letras_incorretas.append(chute)
        total_tentativas -= 1
        if chute == "":
            print("\nEntrada incorreta.")
            print(f"Letra errada! Tentativas restantes: {total_tentativas}")
            print("---------------------------------------")
        else:
            print(f"\nLetra errada! Tentativas restantes: {total_tentativas}")
            print(f"Letras erradas até agora: {letras_incorretas}")
            print("---------------------------------------")

else:
    print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")