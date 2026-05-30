users = []

while True:
    user = input("What is your name? ")
    if user:
        users.append(user + "\n")
    else:
        break

with open("names.txt", "a+") as file:
    file.writelines(users)
    data = file.read(5)
    print(type(data), id(data))
    print(type(file), id(file))

print(users)
