votos = [0] * 23
while True:
    voto = int(input("Digite o número do jogador (ou 0 para encerrar): "))
    if voto == 0:
        break
    elif voto < 1 or voto > 23:
        print("Voto inválido. Por favor, digite um número entre 1 e 23.")
    else:
        votos[voto - 1] += 1

total_votos = sum(votos)
print("Resultado da votação:")
for i, voto in enumerate(votos):
    if voto > 0:
        print(f"Jogador {i+1}: {voto} votos ({voto / total_votos * 100:.2f}%)")

melhor_jogador = votos.index(max(votos)) + 1
print(f"O melhor jogador foi o número {melhor_jogador}, com {max(votos)} votos ({max(votos) / total_votos * 100:.2f}% do total de votos).")