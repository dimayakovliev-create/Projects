from random import randrange


class Point:
    def __init__(self, x, y):
        # Задаем начальные значения защищенным переменным
        self._x = None
        self._y = None
        # Вызываем сеттеры для проверки и записи данных
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self._x = x  # ЗАПИСЬ: используем _x, чтобы избежать рекурсии
        else:
            self._x = None  # СБРОС: записываем None в переменную объекта

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self._y = y  # ЗАПИСЬ: используем _y, чтобы избежать рекурсии
        else:
            self._y = None  # СБРОС: записываем None в переменную объекта
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    

class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Index out of range. Use 0 for x and 1 for y.")
    
    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Index out of range. Use 0 for x and 1 for y.")
    
  
    def __call__(self, value = None):
        if value:
            self.coordinates.x *= value
            self.coordinates.y *= value
            return (self.coordinates.x, self.coordinates.y)
       
       
    def __add__(self, vector):
            x = self.coordinates.x + vector.coordinates.x
            y = self.coordinates.y + vector.coordinates.y
            return Vector(Point(x, y))
       
    def __sub__(self, vector):
            x = self.coordinates.x - vector.coordinates.x
            y = self.coordinates.y - vector.coordinates.y
            return Vector(Point(x, y))

    def __mul__(self, vector):
            scalar = self.coordinates.x * vector.coordinates.x + self.coordinates.y * vector.coordinates.y
            return scalar
                     
    def __str__(self):
        return f"Vector({self.coordinates.x}, {self.coordinates.y})"


      
class Iterable:
    def __init__(self, max_vectors, max_points):
        self.max_vectors = max_vectors
        self.max_points = max_points
        self.current_index = 0
        self.vectors = []
        
        # Заповнюємо список випадковими векторами довжиною max_vectors
        for _ in range(self.max_vectors):
            # randrange(0, max_points + 1) генерує числа в діапазоні 0...max_points
            random_point = Point(randrange(0, self.max_points + 1), randrange(0, self.max_points + 1))
            self.vectors.append(Vector(random_point))

    def __next__(self):
        # Перевіряємо, чи поточний індекс не вийшов за межі кількості векторів
        if self.current_index < self.max_vectors:
            vector = self.vectors[self.current_index]
            self.current_index += 1  # Зміщуємо покажчик на наступний елемент
            return vector
        else:
            # Якщо вектори закінчилися, викликаємо виключення для зупинки циклу
            raise StopIteration


# Об'єкт, що ітерується
class RandomVectors:
    def __init__(self, max_vectors: int, max_points: int):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        # Метод __iter__ повертає новий об'єкт-ітератор класу Iterable
        return Iterable(self.max_vectors, self.max_points)

# Проверка работы кода
point = Point(5, 10)
print(point.x)  # Выведет: 5
print(point.y)  # Выведет: 10

# Проверка некорректных данных
bad_point = Point("строка", [1, 2])
print(bad_point.x)  # Выведет: None
print(bad_point.y)  # Выведет: None

vector = Vector(Point(1, 2))
print(vector.coordinates.x)  # Выведет: 1
print(vector.coordinates.y)  # Выведет: 2
vector[0] = 3
vector[1] = 4

print(vector[0])  # Выведет: 3
print(vector[1])  # Выведет: 4
print(vector)  # Выведет: Vector  (3, 4)
print(point)  # Выведет: Point(5, 10)
print(vector())  # Выведет: (3, 4)
print(vector(8))  # Выведет: (6, 8)
print(vector)  # Выведет: Vector(6, 8)

vector1 = Vector(Point(2, 10))
vector2 = Vector(Point(5, 15))            
print(vector2)

vector3 = vector1 + vector2
vector4 = vector2 - vector1

print(vector1)  # Выведет: Vector(2, 10)
print(vector2)  # Выведет: Vector(5, 15)
scalar = vector1 * vector2
print(scalar)  # Выведет: (2*5 + 10*15) = (10 + 150) = 160
vectors = RandomVectors(5, 10)
for vector in vectors:
    print(vector)