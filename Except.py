from multiprocessing import pool

age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")



# Try - except - else - finally
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = round(pool / quantity)
except ZeroDivisionError:
    print('Divide by zero completed!')
else:
    print(f"Each mailing will receive {chunk} letters.")
