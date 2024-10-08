notas = []
while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)

print(f"Quantidade de valores lidos: {len(notas)}")
print(f"Notas na ordem em que foram informadas: {notas}")
print(f"Notas na ordem inversa: {notas[::-1]}")
print(f"Soma dos valores: {sum(notas)}")
print(f"Média dos valores: {sum(notas) / len(notas)}")
print(f"Quantidade de valores acima da média: {sum(1 for nota in notas if nota > sum(notas) / len(notas))}")
print(f"Quantidade de valores abaixo de sete: {sum(1 for nota in notas if nota < 7)}")