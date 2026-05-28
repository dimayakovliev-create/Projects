import re

text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")


text = "Моя електронна адреса: example@example.com"
pattern = r"\w+\@\w+\.\w+"
match = re.search(pattern, text)
if match:
    print("Електронна адреса:", match.group())



email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)



    email = "username@domain.com, dimayakovliev@gmail.com"
pattern = r"(\w+)@(\w+\.\w+)"
matches = re.findall(pattern, email)

for match in matches:
    user_name = match[0]
    domain_name = match[1]
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)



file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)
print(formatted_name)



text = "Python - потужна, універсальна; мова!"
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)
print(modified_text) 



phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2 \3"
formatted_phone = re.sub(pattern, replacement, phone)
print(formatted_phone)



text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)
print(elements)  # Виведе список частин, розділених пунктуацією


phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)


text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)[:-1:]

print(elements)
