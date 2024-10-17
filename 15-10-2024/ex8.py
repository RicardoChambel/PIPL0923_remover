"""
Faça uma função para imprimir:
a altura deve ser recebida como parametro
 
1
2 2
3 3 3
'''
n n n n n n n ''' n

"""
def piramide(altura):
    for i in range(1, altura + 1):
        for _ in range(i):
            print (i, end=" ")
        print()

piramide(int(input("Insira a altura: ")))