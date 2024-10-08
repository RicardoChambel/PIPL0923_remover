idades = []
alturas = []
for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    altura = float(input(f"Digite a altura do aluno {i+1}: "))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)
contagem = sum(1 for idade, altura in zip(idades, alturas))