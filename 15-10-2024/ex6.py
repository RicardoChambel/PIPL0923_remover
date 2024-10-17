# Crie uma função que conte quantas vezes as letras aparecem numa string
def contarLetras(string) -> int:
    letras = {}
    for letra in string:
        if letra.isalpha():
            if letra in letras:
                letras[letra] += 1
            else:
                letras[letra] = 1

    for letra, quantidade in letras.items():
        print(f"{letra} - {quantidade}")

exemplo1 = "aabbbcccc"
exemplo2 = "aabbbcccc12c"

print("Exemplo 1:")
contarLetras(exemplo1)

print("\nExemplo 2:")
contarLetras(exemplo2)