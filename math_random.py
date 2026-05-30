import math
import random
num = random.random()*100
print(num)

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Карти: {cards}")
print(f"Перша карта: {cards[0]}, Друга карта: {cards[1]}")
print(f"Обрана карта: {random.choices(cards, k=2)}")

colors = ['червоний', 'зелений', 'синій']
weights = [1, 10, 5]
chosen_color = random.choices(colors, weights, k=2)
print(chosen_color)

print(math.pi)
print(math.sqrt(9))
print(math.ceil(3.2))
print(math.floor(3.8))
print(math.pow(2, 3))
print(math.factorial(5))
print(math.gcd(48, 18))

print(math.isclose(0.1 + 0.2, 0.3))
print(math.log(8,2))
print(math.log(math.e))
print(math.log(2))