defesitos = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo ou conector", "quebrado ou inutilizado"]
contagem_defesitos = [0] * 4
while True:
    identificacao = int(input(" Digite a identificação do mouse (ou 0 para encerrar): "))
    if identificacao == 0:
        break
    defeito = input("Digite o defeito do mouse: ")
    while defeito not in defesitos:
        defeito = input("Defeito inválido. Por favor, digite um dos seguintes defeitos: necessita da esfera, necessita de limpeza, necessita troca do cabo ou conector, quebrado ou inutilizado: ")
    contagem_defesitos[defesitos.index(defeito)] += 1

print("Relatório de Defeitos")
print("---------------------")
for i, (defeito, contagem) in enumerate(zip(defesitos, contagem_defesitos)):
    print(f"{i+1} - {defeito}: {contagem} ({contagem / sum(contagem_defesitos) * 100:.2f}%)")