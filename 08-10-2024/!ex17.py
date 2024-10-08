atletas = []
while True:
    nome = input("Digite o nome do atleta (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    saltos = []
    for i in range(5):
        salto = float(input(f"Digite o salto {i+1} do atleta {nome}: "))
        saltos.append(salto)
    atletas.append((nome, saltos))

for nome, saltos in atletas:
    media_saltos = sum(saltos) / len(saltos)
    print(f"Atleta: {nome}")
    print(f"Saltos: {saltos}")
    print(f"Média dos saltos: {media_saltos}")