# Crie uma função que conte quantas vezes as palavras aparecem numa string
def contarPalavras(frase):
    palavras = {}
    letras = frase.split()
    for palavra in letras:
        palavra = palavra.lower()
        if palavra.isalpha():
            if palavra in palavras:
                palavras[palavra] += 1
            else:
                palavras[palavra] = 1

    for palavra, quantidade in palavras.items():
        print(f"{palavra} - {quantidade}")

exemplo1 = "O meu nome é ricardo chambel"
exemplo2 = "Estou na turma PIPL0923"

print("Exemplo 1:")
contarPalavras(exemplo1)

print("\nExemplo 2:")
contarPalavras(exemplo2)    