"""
Peça ao utilizador 10 valores numericos
Vrifique se o valor é numero, se nao for descarte esse valor
Adicione a lista os valroes numericos
Calcule a media dos valores na lista
"""
lista = []
for i in range(10):
    val = "x"
    while not val.isnumeric():
        val = input(f"{i+1} | Introduza um valor numerico: ")
        if not val.isnumeric():
            print("Valor não numerico!")
        else:
            lista.append(val)
print(lista)