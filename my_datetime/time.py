from datetime import date, datetime, time, timezone

print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().date())
print(datetime.now().time())

import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

timedelta = datetime.timedelta(weeks=3, days=4, hours=3)
print(timedelta)  # Виведе "11 days, 3:00:00"
future_date = datetime.datetime.now() + timedelta
print(future_date) 

print(date.toordinal(datetime.datetime.now()))  # Виведе дату і час, що буде через 3
print(datetime.datetime.now().timestamp())  # Виведе кількість секунд, що минули з 1 січня 1970 року

from datetime import datetime

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

timestamp = 1617183600
# Конвертація timestamp в datetime
dt_from_timestamp = datetime.fromtimestamp(timestamp)
print(dt_from_timestamp)  # Виведе datetime з timestamp

formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

print(now.isoformat())
print(now.isoweekday())
print(now.isocalendar())  # Виведе день тижня в ISO форматі
print(datetime.now(timezone.utc))  # Виведе поточний час в UTC


from datetime import datetime, timezone, timedelta, time
utc_time = datetime.now(timezone.utc)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
print("UTC Time:", utc_time)
print("Eastern Time:", eastern_time)

import time
current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

# Вимірювання часу виконання коду
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")