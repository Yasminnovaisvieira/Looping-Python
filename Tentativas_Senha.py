#Simulação de tentativas de senhas.

print("Olá! O programa irá solicitar uma senha e apenas parará de solicitar quando a mesma estiver correta.\n")

while (True):
    senha = str(input("Digite a senha: "))
    if senha == "yasmin":
        print("\nSenha correta!\n")
        break
    else:
        print("\nSenha inválida! Tente novamente.\n")