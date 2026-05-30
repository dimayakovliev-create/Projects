from typing import Callable, Dict

# Визначення функцій
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def power(exponent: int) -> Callable[[int], int]:
    def inner(c: int) -> int:
        return c ** exponent
    return inner

# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

# Словник операцій
operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square, #square = power(2)
    'cube': cube #cube = power(3)
}

# Використання операцій
result_add = operations['add'](10, 20)  # 30
result_square = operations['square'](5)  # 25
result_cube = operations['cube'](5)  # 125
result_multiply = operations['multiply'](10, 20)  # 200

print(result_add)  
print(result_square)  
print(result_cube)  
print(result_multiply)


def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

# Використання
square = power(2)
cube = power(3)

print(square(5)) 
print(cube(5)) 

def make_formatter(prefix: str, suffix: str) -> Callable[[str], str]:
    def formatter(text: str) -> str:
        return f"{prefix}{text}{suffix}"
    return formatter

# Создаем функции форматирования
render_html_bold = make_formatter("<b>", "</b>")
render_tweet = make_formatter("[NEWS] ", " #trending")
render_email = make_formatter("From: ", "@example.com")

print(render_html_bold("Привіт"))  # <b>Привет</b>
print(render_tweet("Текст"))       # [NEWS] Текст #trending
print(render_email("john"))  # From: john@example.com   


def outer_function(msg): # msg - це змінна, яка знаходиться в області видимості зовнішньої функції outer_function і доступна для внутрішньої функції inner_function завдяки замиканню (closure). Коли ми викликаємо inner_function, вона має доступ до змінної message, навіть після того, як outer_function завершила своє виконання.
    message = msg

    def inner_function():
        print(message,"From inside ;)") # Виведе "Hello, world!" при виклику inner_function

    return inner_function

# Створення замикання
my_func = outer_function("Hello, world!")
my_func()

# Створення словника з функціями знижок (currying):
from typing import Callable, Dict

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30),
    "40%": discount(40)
}

# Використання функції зі словника
price = 500
discount_type = "40%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price} грн")

# Створення списків з використанням синтаксису генераторів списків (list comprehensions):
sq = [i**2 for i in range(1, 6)]
print(sq)
even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)
sq = {i: i**2 for i in range(1, 10)}
print(sq)
