"""
    w - write
    r - read
    a - append

    x - cria

    t- txt
    v - bin
    """
l = (1,2,3)


def myFune(n):
    if n == 0:
        Exception(" n nao pode ser o")

    print("myFune - it Works !!") 

try:
    myFune(0)
    print(l[9])
    file = open("demo.txt", "xt")

except FileExistsError as e:
    print(f"O file já existe - {e.filename}")

except IndexError as e:
    print(f"IndexError: list index out of range - {e}")

except Exception as e:
    print(e)


print("it Works!!")