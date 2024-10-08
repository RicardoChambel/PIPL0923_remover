vetor1 = [int(input(f"Digite o número {i+1} do vetor 1: ")) for i in range(10)]
vetor2 = [int(input(f"Digite o número {i+1} do vetor 2: ")) for i in range(10)]
vetor3 = [x for pair in zip(vetor1, vetor2) for x in pair]

print(f"Vetor 3: {vetor3}")