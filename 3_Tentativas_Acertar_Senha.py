#Apenas 3 tentativas para acertar a senha.

print("Olá! O programa aceitará apenas 3 tentativas para acertar a senha.\n")

tentativa = 1

while(tentativa <= 3):
    resposta = str(input(f"Digite a sua {tentativa}ª tentativa: "))

    if resposta == "yasmin":
        print("Senha correta!")
        break
    else:
        print(f"Senha incorreta! Tente novamente.")

    tentativa += 1