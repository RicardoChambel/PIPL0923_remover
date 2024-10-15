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

# Type cast






#funcs