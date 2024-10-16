my_dict = {'Natasha': 2002, 'Misha': 1998, 'Sveta': 1999} # словарь
print(my_dict)
print(my_dict ['Misha'])
my_dict.update({'Masha' : 2004,
                'Andrey': 2003})
print(my_dict)
my_set = {1, 0.1, True, 'Coffe', 1, 78, 'Coffe', 13, 'DVD'} # множество
print(my_set)
my_set.update([5, 2, False]) # добавляет несколько элементов
print(my_set)
my_set.add('name') # добавляет один элемент
print(my_set)
my_set.discard(0.1) # удаляется 0,1 из множества
print(my_set)
my_set. remove(2)# удаляет 2 из множества (даст знать, если нет такого элемента)
print(my_set)
