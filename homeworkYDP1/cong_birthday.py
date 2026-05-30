from calendar import weekday
from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Michael Williams", "birthday": "1995.05.15"},
    {"name": "Monika Loyd", "birthday": "1989.05.17"}
]


def get_upcoming_birthdays(users):
    today = datetime.today().date() # виводимо поточну дату без часу
    upcoming = []
    for user in users:
        # Перетворюємо строку в об'єкт дати та навпаки (для подальшого порівняння кількості днів та пошуку "Неділі")
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # перетворюємо параметр "birthday" в формат дати народження (без часу)
        birthday_this_year = bday.replace(year=today.year) # замінюємо рік народження на поточний рік (щоб не зштовхнутися з проблемою вирахування високосних років)
        weekday_this_year = birthday_this_year.weekday() # пошук номеру дня тижнянародження в поточному році (пвертає 6 якщо неділя)
        days_until = (birthday_this_year - today).days # вираховує різницю в днях між датою народження та поточною датою
        if 0 <= days_until <= 7: # перевіряється умова найближчого ДР
            if weekday_this_year == 6: # перевіряється умова, чи не припадає ДР на Неділю
                congrat_date = birthday_this_year + timedelta(days=1) # зсувається дата привітання на 1 день вперед у разі якщо день тижня дорівнює 6 (Неділя)
            else:
                congrat_date = birthday_this_year # повертається дата привітання, якщо день тижня не припадає на Неділю
            #
            upcoming.append({"name": user["name"], "congratulation_date": congrat_date.strftime("%Y.%m.%d")})
    return upcoming
# Виводиться результат на друк (як вимагається за форматом у задачі)
upcoming = get_upcoming_birthdays(users)
print(upcoming)

# Результат виводиться на друк для зручності використання у роботі
print("Список привітань в найближчі 7 днів:")
for user in upcoming:
    name = user["name"]
    congratulation_date = user["congratulation_date"]
    print(f"{name:<20} |  {congratulation_date}")