# Crie uma função que some todos os valores de uma lista de inteiros

listaRes = [1,2,3,4,5] # <- Lista

# Sem método sum()
def sum_lista(lista) -> int:
    add = 0
    for i in lista:
        resultado = i + add
        add = resultado
    print(f"Soma da lista ( Com função ): {resultado}")

sum_lista(listaRes)# <- Print sem método sum()

# Com método sum()
def sum_lista2(lista) -> int:
    sum(lista)
    print(f"Soma da lista ( Sem função ): {sum(listaRes)}")


sum_lista2(listaRes)# <- Print com método sum()