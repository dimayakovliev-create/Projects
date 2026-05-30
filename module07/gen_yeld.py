def count_down(start):
    while start > 0:
        yield start
        start -= 1

for number in count_down(0):
    print(number)

def read_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip() # Видаляємо зайві пробіли та символи нового рядка з кожного рядка перед поверненням його генератором

# Використання генератора для читання рядків з файлу
for line in read_lines("module07/my_file.txt"):
    print(line)