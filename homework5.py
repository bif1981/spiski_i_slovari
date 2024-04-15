my_list = ['Banana', 'Orange', 'Apple', 'Pineapple', 'Apricot', 'Kiwi', 'Avocado'] # Создаю список
print(f'List:', (my_list))              # Вывожу на экран список my_list
print(f'First element:', my_list[0])    # Вывожу на экран первый и последний элементы списка my_list
print(f'Last element:', my_list[-1])
print(f'Sublist:', my_list[3:6])        # Вывожу на экран подсписок my_list с третьего до пятого элементов
my_list[3] = 'Grapefruit'               # Изменить значение третьего элемента списка my_list
print(f'Modified list:', my_list)      # Вывожу на экран измененный список my_list

print('--------------------------------------------------------------------------')

my_dict = {                     # Создаю словарь
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 5,
    'Six': 6,
    'Seven': 7
    }
print('Dictionary:', my_dict)                  # Вывожу на экран словарь my_dict
print(f'Translation:', my_dict['Two'])         # Вывожу на экран значение для заданного ключа в my_dict
my_dict['One'] = 1                             # Изменил значение для заданного ключа  в my_dict
my_dict['Eight'] = 'Восемь'                    # Добавил новое ключ-значение в my_dict
print(f'Modified dictionary:', my_dict)        # Вывожу на экран измененный словарь my_dict