from io import TextIOWrapper
import os
from os import close
import shutil

fh = open('module05/file_test.txt', 'r', encoding='utf-8')
print(fh.read())
print(fh.tell())
fh.seek(0)
print(fh.read(10))
print(fh.tell())
fh.close()



fh = open('test.txt', 'w')
symbols_written = fh.write('Hello World! ')
print(symbols_written) # 6
fh.close()

fh = open('test.txt', 'a+')
fh.write('How are you?')
fh.seek(0)

first_two_symbols = fh.read()
print(first_two_symbols)  # 'he'

fh.close()


with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)

with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

string = 'Hello world!'
byte_string = string.encode(encoding="utf-8", errors="strict")
byte_code = list(byte_string)
for char, code in zip(byte_string, byte_code):
    print(f"Символ: {char} -> Код байта: {code}")
print(byte_string)
print(byte_code)

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел
print(ord("f"))
print(chr(78))

print(b'Hello world!'.decode('utf-16'))

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)

byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))
print(byte_array)

byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'




s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(f"from utf-16: {s_from_utf16}")
print(s_from_utf16 == s)





text = "PythoN ProgrAmmIng"
print(text.casefold())

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")



# shutil.make_archive('example', 'zip', root_dir='module05')
# shutil.make_archive('example', 'gztar', root_dir='module3')
# shutil.unpack_archive('example.zip', 'destination_folder')
# shutil.copy('example.zip', 'module05')
# shutil.move('OlegAndrus', 'my_new')
# shutil.rmtree('destination_folder')
# shutil.disk_usage('.')