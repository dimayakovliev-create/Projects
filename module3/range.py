import random
def car_numbers():
    set_letters = list('ABEKMHOPCTYX')
    set_digits = random.randint(1000, 9999)
    p1 = random.choices(set_letters, k=2)
    p1 = "".join(p1)
    p2 = set_digits
    p3 = random.choices(set_letters, k=2)
    p3 = "".join(p3)
    return f"{p1} {p2} {p3}"
car_numbers()
print(car_numbers())