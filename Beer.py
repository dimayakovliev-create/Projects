customer = input("What is your name? ")
age = int(input("What is your age? "))
if age == 18:
    message = f"Congratulations {customer}, you are now an adult! Take your first beer and enjoy!"
elif age > 18:
    message = f"Hello {customer}, you are already {age} years! Enjoy your beer!"
else:    
    message = f"Sorry {customer}, you are only {age} years old. You cannot drink beer yet!"
print(message)