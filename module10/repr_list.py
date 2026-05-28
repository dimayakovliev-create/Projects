from collections import UserList

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(2, 3)
print(repr(point))  # Виводить: Point(x=2, y=3)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def res(self):
        return f"Point(x={self.x}, y={self.y})" # Метод для отримання рядкового представлення об'єкта

point = Point(2, 3)
print(point.res())  # Виводить: Point(x=2, y=3)

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Human({self.name}, {self.age})"

human = Human("Alice", 30)
print (str(human))  # Викликає __str__: Human named Alice who is 30 years old
print (repr(human))  # Викликає __repr__: Human(Alice, 30)
print (human)  # Викликає __str__ за замовчуванням: Human named Alice who is 30 years old

class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Dima'
simple_dict['age'] = 25, 30
simple_dict['city'] = 'Kyiv'
simple_dict['country'] = 'Ukraine'

print(simple_dict['name'])  
print(simple_dict['age'])  
print(simple_dict['city'])  
print(simple_dict['country'])  # Спроба отримати неіснуючий ключ
print(simple_dict ['occupation'])  # Спроба отримати неіснуючий ключ


class BoundedList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()

    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)

    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")

    def append(self, item):
        self.__validate_item(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)

    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    temperatures = BoundedList(18, 26, [19, 21, 25])  # Викликає ValueError через 28
    print(temperatures)

    for el in [20, 22, 25, 27, 30, 17, 10, 18, 26]:
        try:
            temperatures.append(el)
        except ValueError as e:
            print(e)

    print(temperatures)
