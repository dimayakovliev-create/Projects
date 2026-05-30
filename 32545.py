num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))
total_cost = num_croissants * 1.5 + num_glasses * 2.0 + num_coffee_packs * 3.0

total_dollars = int(total_cost)
total_cents = int(total_cost * 100)
print(f"Total cost in dollars: {total_dollars}")
print(f"Total cost in cents: {total_cents}")