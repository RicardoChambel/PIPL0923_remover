"""
Faça uma função para imprimir, deve receber como parametro o numero de niveis:

1
2 2
3 3 3
4 4 4 4

---

n n n n n n n n n n n ... n vezes

"""

def piramide(altura: int):
    print("-"*15)
    print("Piramide criada:")

    for i in range(altura + 1):
        print(f"{i} " * i)

    print("-"*15)

altura = int(input("Insira a altura da piramide: "))
piramide(altura)