votos = [0] * 6
while True:
    voto = int(input("Digite o número da opção (ou 0 para encerrar): "))
    if voto == 0:
        break
    elif voto < 1 or voto > 6:
        print("Voto inválido. Por favor, digite um número entre 1 e 6.")
    else:
        votos[voto - 1] += 1

total_votos = sum(votos)
print("Resultado da enquete:")
opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
for i, voto in enumerate(votos):
    print(f"{opcoes[i]}: {voto} votos ({voto / total_votos * 100:.2f}%)")

vencedor = opcoes[votos.index(max(votos))]
print(f"O vencedor da enquete foi {vencedor}, com {max(votos)} votos ({max(votos) / total_votos * 100:.2f}% do total de votos).")