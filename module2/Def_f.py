def print_max(a:int, b:int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

a = input("Введіть перше число X: ")
b = input("Введіть друге число Y: ")

print_max(a, b)  # передача змінних у якості аргументів
