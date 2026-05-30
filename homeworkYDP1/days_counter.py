from datetime import datetime

def get_days_from_today(date):
    while True:
        try:
            d_1 = datetime.strptime(date, "%Y-%m-%d").date() # перетворюємо введені дані в формат дати (без часу)
            date_now = datetime.now().date()
            diff = date_now - d_1 #
            return diff
        except (AttributeError, ValueError): # ПОвідомляємо про помилку у разі введення або невірної дати або дати в невірному форматі
            print("Помилка! Невірний формат дати. Спробуйте ще раз в форматі РРРР-ММ-ДД!")
        return None
   

date = input("Введіть дату події в форматі РРРР-ММ-ДД: ")
result = get_days_from_today(date) # виконується функція розрахунку кількості днів
while True:
    if result is not None: 
        if result.days > 0: #
            print("Від дати події до сьогодні минуло ", result.days, " дні(в).")
        elif result.days < 0: #
            print("Від сьогодня до дати події залишається ", result.days, " дні(в).")
        else:
            print("Ваша подія відбувається сьогодні!") #
    break # Виходимо з циклу коли ввели невірний формат (слова, символи, тощо)
