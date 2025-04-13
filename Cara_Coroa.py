# Moeda: Cara ou Coroa.

import random

print("Olá! O programa irá lançar 'Cara' e 'Coroa' até sair 'Cara' três vezes seguidas.\n")

caras = 0

while(True):
    resultado = random.choice(["Cara", "Coroa"])
    print(f"Lançamento: {resultado}")
    if resultado == "Cara":
        caras += 1
    else:
        caras = 0

    if caras >= 3:
        print("'Cara' apareceu 3 vezes seguidas!")
        break