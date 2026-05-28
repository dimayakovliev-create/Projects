from collections import namedtuple, Counter, defaultdict, deque
import collections

Persons = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])
person1 = Persons(first_name='John', last_name='Doe', age=30, birth_place='New York', post_index='10001')
print(person1.first_name)  # John
print(person1.last_name)   # Doe
print(person1.age)         # 30
print(person1[3])  # New York
print(person1.post_index)   # 10001
person2 = Persons(first_name='Jane', last_name='Smith', age=25, birth_place='Los Angeles', post_index='90001')
# print(person2.first_name)  # Jane
# print(person2.last_name)   # Smith
# print(person2.age)         # 25
# print(person2.birth_place)  # Los Angeles
# print(person2.post_index)   # 90001
print(Persons._fields)  # ('first_name', 'last_name', 'age', 'birth_place', 'post_index')
print(person1._asdict())  # {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'birth_place': 'New York', 'post_index': '10001'}

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 1, 1, 1, 3, 5]
mark_counts = {}
for i in student_marks:
    if i in mark_counts:
        mark_counts[i] += 1
    else:
        mark_counts[i] = 1

mark_counts1 = collections.Counter(student_marks)
print(mark_counts)
print(mark_counts1)
print(mark_counts1.most_common(1))

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)   
d['b'].append(5)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [5]})

d = defaultdict(int) # Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 11
d['a'] += 1
d['c'] += 78
print(d)

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix', 'zebra', 'leopard']
grouped_words = {}

for word in words:
    char = word[0]  # Беремо перший символ слова
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)
print(grouped_words)

grouped_words = defaultdict(list)
for word in words:
    char = word[0]  # Беремо перший символ слова
    grouped_words[char].append(word) # defaultdict автоматично створює порожній список для кожного нового ключа, тому ми можемо безпосередньо додавати слова до відповідного списку, не перевіряючи наявність ключа в словнику.
print(grouped_words)