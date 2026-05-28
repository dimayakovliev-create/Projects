class Point:
    def __init__(self, x, y):
        # Инициализация через сеттер, который проверяет значения
        self.value = (x, y)

    @property
    def value(self): 
        return self.__x, self.__y  
    
        # Сеттер для установки новых значений с проверкой
    @value.setter
    def value(self, new_value):
        x, y = new_value
        if x > 0 and y > 0:
            self.__x = x
            self.__y = y
        else:
            self.__x, self.__y = 0, 0
            print('Only numbers greater zero accepted!!!')

    
# Проверка работы кода
point = Point(-5, 10)
print(point.value)  # Выведет: (0, 0)
point = Point(15, 10) # Выведет: Only numbers greater zero accepted
print(point.value)  # Выведет: (15, 10)