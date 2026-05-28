from collections import deque

# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елемента
def push(stack, item):
    stack.append(item)

# Вилучення елемента
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")

stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
print(peek(stack))  # c
print(pop(stack))   # c
print(peek(stack))  # b

from collections import deque

# Створення пустої двосторонньої черги
d = deque()

# Додаємо елементи в чергу
d.append('middle')  # Додаємо 'middle' у кінець черги
d.append('last')    # Додаємо 'last' у кінець черги
d.appendleft('first')  # Додаємо 'first' на початок черги

# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d))
# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop())
# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft())
# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d))

tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]

task_queue = deque()
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додаємо швидкі завдання на початок черги
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додаємо повільні завдання в кінець черги
        print(f"Додано повільне завдання: {task['name']}")
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")
    
print("Черга завдань:", list(task_queue))   