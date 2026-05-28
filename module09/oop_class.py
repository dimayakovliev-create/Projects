class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age

bob = Person('Boris', 34)
alice = Person('Alice', 28)

bob.say_name()
bob.set_age(35)
bob.say_name()
alice.say_name()
alice.set_age(30)
alice.say_name()


class Person:
    count = 2
k = 8
person = Person()
person.count = Person.count + k
print(person.count)  # 10
print(Person.count)  # 2


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin

        
p = Person("Boris", 34, True, False)
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())

class Animal:
    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed

    def make_sound(self):
        pass

class Cat(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)

    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)

    def make_sound(self):
        return "Woof"
    
    def chase_tail(self) -> str:
        return f"{self.name} is chasing its tail!"

class Cow(Animal):  
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age, breed)

    def make_sound(self) -> str:
        return "Moo"

my_cat = Cat("Simon", 4, "Siamese")
my_dog = Dog("Rex", 5, "Golden Retriever")
my_cow = Cow("Bessie", 3, "Holstein")

print(my_cat.make_sound())  # Виведе "Meow"
print(my_dog.make_sound())  # Виведе "Woof"
print(my_cow.make_sound())  # Виведе "Moo"
for animal in [my_cat, my_dog, my_cow]:
    print(f"Имя: {animal.name}, Возраст: {animal.age}, Порода: {animal.breed}, Звук: {animal.make_sound()}")
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Parrot(Bird):
    def can_fly(self):
        return True

class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"

my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, Dimas!"))

class A:
    teacher = "Мій вчитель Viktor"

class B:
    name = "Я клас B"
    property = "Я знаходжусь у класі B"
    teacher = "Мій вчитель: Dimas"

class C(A, B):
    property = "Я знаходжусь у класі C"

c = C()
print(c.name)
print(c.property)
print(c.teacher)