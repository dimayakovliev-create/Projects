import random

def get_numbers_ticket(min, max, quantity):
    try:
        lots = list(range(min, max+1))
        return random.sample(lots, quantity)
    except ValueError: # Обробка помилок, якщо заводиться відємне значення або кількість виборки перевищує загальну кількість номерів
        print("Кількість обраних чисел перевищує загальну, або її значення - від'ємне!")
        return exit()
    
while True:
    try:
        max_num = int(input("Введіть максимальну кількість чисел у лотереї: "))
        max_num = 1000 if max_num > 1000 else max_num
        quantity = abs(int(input("Введіть кількість чисел які потрібно вибрати: ")))
        break  # Якщо все ввели правильно, виходимо з циклу
    except ValueError: # Обробка помилки введення не числового значення (символи, букви, тощо)
        print("Це не число! Спробуйте ще раз!")

result = print("Комбінація на лототроні наступна: ",get_numbers_ticket(1, max_num, quantity))