from ast import arg


def modify_list(u_lst: list) -> None:
    u_lst.append(4)
    u_lst.pop(3)
    u_lst.insert(2,12)
    u_lst[0] = 36
    return u_lst

my_list = [1, 2, 3, 5, 10]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 5, 7, 4]

def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

result = string_to_codes("Hello, World!")
print(result)  # Виведе словник з символами та їх кодами

def greet(name, message="Привіт", times=3):
    print((f"{message}, {name}! ")*times)
  
greet("Олексію")  # Використовує значення за замовчуванням для message

def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)
print("Початкова ціна на хліб", real_cost(1000))  # Використовує значення за замовчуванням для discount
print("Ціна на хліб зі знижкою", real_cost(1000, 0.1))  # Вказує власне значення для discount

def example_function(*args, **kwargs):
        print("Позиційні аргументи:", args)
        print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)  # Використання *args та **kwargs

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Alice", "age": 25}
greet(**person_info)
