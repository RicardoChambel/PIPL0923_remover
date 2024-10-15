#var
# tipos de dados (int, float, str ....)
# if
# elif
# else
# match
# while
# tuplos
# list (arrays)
# Sets
# None
# dict
'''

[(K,v),(K,v),(K,v)]


'''

"""
list - []
set - {}
dict = {"K": "v"}


"""

lista = ["Value1", "Value2", "Value3"]
print(lista[0])

mySet = ["Value1", "Value2", "Value3"]
print(mySet)

infos = {"key": "value 1", "key2": "value 2", "key3": "value 3" , "key4": "value 4", "key5": "value 5"}
print(f"key1: {infos["key"]}")
print(f"key2: {infos["key2"]}")
print(f"key3: {infos.get("key3")}")

print(f"key5: {infos.get('key5') is not None}")
print(f"outra key5: {infos.get('outra key5') is None}")

print(infos)
print("--- print(infos.keys()) ---")
print(infos.keys())

print("--- print(infos.values()) ---")
print(infos.values())

print("--- print(infos.items()) ---")
print(infos.items())

print("key" in infos)
print("key" in infos.keys())
print("key" in infos.values())

print(("key", "value1") in infos.items())

print("---------------------------- Mudar valor ----------------------------")
print(f"Key: {infos["key"]}")

infos["key"] = "Novo Valor"

print(f"Key: {infos["key"]}")


print("---------------------------- Add valor ----------------------------")

print(infos)

infos["Nova Key"] = "Novo VALOR 2"

print(infos)

print("---------------------------- Remove vals ----------------------------")
print(infos.keys())

infos.pop("Nova Key")
print(infos.keys())

del infos["key4"]
print(infos.keys())


print("---------------------------- Remove vals (key nao existe) ----------------------------")
#del infos["key4"] <- erro
#infos.pop("Nova Key") <- erro

print(infos)

infos.clear()

print(infos)

escola = "ATEC"

d1 = {"nome":"Gonçalo","Escola":escola}
d2 = {"Turma1":"PIPL0923","Turma2":"PIPL0922"}

print(f"d1           : {d1}")
print(f"d2           : {d2}")

d1.update(d2) # <---- UPDATE D1 COM D2
print(f"d1.update(d2): {d2}")


print("-------- Loops ---------")

myList = [1,2,3,4,5,6,7,8,9,10]

for elm in myList:
    print(elm) 

print("-------- Loops dict ---------")


for elm in d1:
    print(elm) # keys


print("---------")
for elm in d1.keys():
    print(elm) # keys


print("---------")
for elm in d1.keys():
    print(d1[elm]) # valores


print("----- for elm in d1.keys(): -----")
for elm in d1.values():
    print(elm)


print("----- for elm in d1.values(): -----")
for elm in d1.values():
    print(elm)

# Type cast





#funcs