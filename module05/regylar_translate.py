intab = "abcdefghijklmnopqrstuvwxyz"
k = 5
outtab = intab[k:26] + intab[0:k]
trantab = str.maketrans(intab, outtab,",.!?")
print("Таблиця перекладу:", trantab)
str = "This is string example!"
print(str.translate(trantab))

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]
MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c
    print("Таблиця перекладу:", MAP)
sixteen = "1a3F"
print("Переклад рядка:", sixteen.translate(MAP))

for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)


