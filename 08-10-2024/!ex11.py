vetor1 = [int(input(f"Digite o número {i+1} do vetor 1: ")) for i in range(10)]
vetor2 = [int(input(f"Digite o número {i+1} do vetor 2: ")) for i in range(10)]
vetor3 = [int(input(f"Digite o número {i+1} do vetor 3: ")) for i in range(10)]
vetor4 = [x for triplet in zip(vetor1, vetor2, vetor3) for x in triplet]

print(f"Vetor 4: {vetor4}")