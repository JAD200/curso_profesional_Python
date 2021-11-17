print("""\n Como se comportan los sets """)
my_set = {3, 4, 5}#* Expected uotput:
print('my_set =', my_set)# my_set = {3, 4, 5}

my_set2 = {"Hola", 23.3, False, True}#* Expected uotput:
print('my_set2 =', my_set2)# my_set2 = {'Hola', False, True, 23.3}

my_set3 = {3, 3, 2}#* Expected uotput:
print('my_set3 =', my_set3)# my_set3 = {2, 3}

# my_set4 = {[1, 2, 3], 4}#! Expected uotput:
# print('my_set4 =', my_set4)# TypeError: unhashable type: 'list'


print("""\n Declarar un set """)
empty_set = {}#* Expected output:
print(type(empty_set))# <class 'dict'>

empty_set = set()#* Expected output:
print(type(empty_set))# <class 'set'>


print("""\n Casting con sets """)
my_list = [1, 1, 2, 3, 4, 4, 5]
my_set = set(my_list)#* Expected output:
print(my_set)# {1, 2, 3, 4, 5}

my_tuple = ("Hola", "Hola", "Hola", 1)# Deletes the repeated elements
my_set2 = set(my_tuple)#* Expected output:
print(my_set2)# {'Hola', 1}


print("""\n Añadir elementos a un set """)
my_set = {1, 2, 3}#* Expected output:
print(my_set)#  {1, 2, 3}

# Add one element
my_set.add(4)#* Expected output:
print(my_set)# {1, 2, 3, 4}

# Add many elements
my_set.update([1, 2, 5])#* Expected output:
print(my_set)# {1, 2, 3, 4, 5}

# Add multiple elements
my_set.update((1, 7, 2), {6, 8})#* Expected output:
print(my_set)# {1, 2, 3, 4, 5, 6, 7, 8}


print("""\n Borrar elementos de un set""")
my_set = {1, 2, 3, 4, 5, 6, 7}#* Expected output:
print(my_set)# {1, 2, 3, 4, 5, 6, 7}

# Erase one existing element
my_set.discard(1)#* Expected output:
print(my_set)# {2, 3, 4, 5, 6, 7}

my_set.remove(2)#* Expected output:
print(my_set)# {2, 3, 4, 5, 6, 7}

# Erase one non existing element
my_set.discard(10)#* Expected output:
print(my_set)# {3, 4, 5, 6, 7}

# my_set.remove(12)#! Expected output:
# print(my_set)# KeyError: 12

print('\n')
my_set = {1, 2, 3, 4, 5, 6, 7}#* Expected output:
print(my_set)# {1, 2, 3, 4, 5, 6, 7}

# Erase first element
my_set.pop()#* Expected output:
print(my_set)# {2, 3, 4, 5, 6, 7}

# Clean the whole set
my_set.clear()#* Expected output:
print(my_set)# set()