foo = 1
for i in range(5):
    j = i
    if i % 2 == 0:
        j = 4

    print(f"Ola Mundo, {foo + j}")