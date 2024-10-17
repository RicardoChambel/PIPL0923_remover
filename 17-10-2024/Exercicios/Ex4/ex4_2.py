"""
Faça uma função para imprimir, deve receber como parametro o numero de niveis:

1
1 2
1 2 3
1 2 3 4

---

1 2 3 4 5 6 7 8 9 10 ... 10 vezes

"""

def piramide(altura: int):
    print("-"*15)
    print("Piramide criada:")

    for i in range(1, altura + 1):
        x = ""
        for num in range(1, i + 1):
            x += f"{str(num)} "
        print(x)
    
    print("-"*15)

altura = int(input("Insira a altura da piramide: "))
piramide(altura)