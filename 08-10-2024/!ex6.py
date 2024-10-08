# CALCULAR MEDIA
alunos = []

for i in range(10):

    notas = []

    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)

    alunos.append((i+1, (sum(notas) / len(notas))))

contagem = sum(1 for _, media in alunos if media >= 7.0)

print(f"Alunos com média maior ou igual a 7.0: {contagem}")