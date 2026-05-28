# прогон цикла от 0 до 100 и суммирование всех чисел
num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0:
    sum = sum + num
    num = num - 1
print(sum)


# пошук кількості входжень символу "r" у рядку
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "n"
result = 0
for char in message:
    if char.lower() == search:
        result +=1
print("Total number of ", search, "is ", result)


# функція для запрошення на захід
def invite_to_event(username):
    message = f"Dear {username}, we have the honour to invite you to our event!"
    return message
username = "Oleg"
print(invite_to_event(username))


# функція для обчислення знижки на товар
def discount_price(price, discount):
    
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount()    
    return price

print(discount_price(1000, 0.1))  # Виведе: 900.0


# функція для форматування рядка з центруванням
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        space_bar = (length - len(string)) // 2
        return (" "*space_bar) + string

print(format_string("aaaaaaaaaaaaaaaaac", 40))



# функція для обчислення кількості аргументів, переданих у вигляді позиційних та іменованих
def first(size, *args):
    amount = size + len(args)
    return amount
print(first(4, "first", "second", "third"))

def second(size, **kwargs):
    amount = size + len(kwargs)
    return amount
print(second(2, key1 = "Dmytro", key2 = "Ivan", key3 = "Mykhaylo"))


# функція для обчислення кількості комбінацій з n елементів по k
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    winners = factorial(n) // (factorial(k) * factorial(n - k))
    return winners

print(number_of_groups(10, 3))  # Виведе: 120 
