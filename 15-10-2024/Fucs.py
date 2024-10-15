def ola_mundo():
    print("Ola Mundo")

ola_mundo()
ola_mundo()
ola_mundo()
ola_mundo()

def ola_mundo_v2(nome):
    print(f"Ola mundo, {nome}")

ola_mundo_v2("Ricardo")
ola_mundo_v2("Daniel")
ola_mundo_v2("Ivan")

num = 12

def ola_mundo_v3(nome: str, ano: int, idade:int):
    print(f"Ola mundo, {nome}, {ano}")

ola_mundo_v3("Ricardo", 2000, 80)

def soma(valor1:int, valor2:int) -> int:
    return valor1+valor1

res = soma(3, 4)
print(res)

res2 = soma(3.5, 4.5)
print(res2)

res3 = soma("3.5","4.5")
print(res3)