def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    winners = factorial(n) // (factorial(k) * factorial(n - k))
    return winners

print(number_of_groups(10, 6))  # Виведе: 252


