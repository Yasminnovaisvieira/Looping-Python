#Mostrar Menu até o usuário desejar sair.

print("Olá! O programa irá oferecer um Menu até a opção de saída ser selecionada.\n")

while(True):
    print("######################\n     CALCULADORA\n(A) - Soma\n(B) - Subtração\n(C) - Multiplicação\n(D) - Divisão\n(X) - SAIR\n######################")
    resposta = str(input("\nDigite a opção que deseja: "))
    if resposta == 'x' or resposta == 'X':
        print("\nFinalizando...")
        break