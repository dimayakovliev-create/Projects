def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache: # Якщо результат для n вже обчислений, повертаємо його з кешу
            return cache[n] 
        if n <= 1:           # Якщо n менше або дорівнює 1, повертаємо n (0 або 1)
            return n
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result # Зберігаємо обчислений результат у кеші перед поверненням
        return result

    return fibonacci


# Отримуємо функцію fibonacci з кешуванням через замикання:
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(12))  # Виведе 144
print(fib(15))  # Виведе 610, але тепер швидко, оскільки результат збережено в кеші