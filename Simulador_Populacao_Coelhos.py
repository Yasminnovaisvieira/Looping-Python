# Simula a quantidade de coelhos em cada geração com base nos dados solicitados.

print("##### Simulador de População de Coelhos #####\n")

populacao = int(input("Digite a quantidade inicial de coelhos: "))
taxa_reproducao = float(input("Digite a taxa de reprodução (% por geração): "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade (% por geração): "))
geracoes = int(input("Digite o número de gerações que deseja a simulação: "))

print("\n------- Simulação -------")

for i in range(1, geracoes + 1):
    nascimentos = populacao * (taxa_reproducao / 100)
    mortes = populacao * (taxa_mortalidade / 100)
    populacao = populacao + nascimentos - mortes

    print(f" Geração {i}: {int(populacao)} coelhos")

print("------- Simulação -------")
