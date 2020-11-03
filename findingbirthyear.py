from datetime import date

# gathering user data
name = input("What is your name? ").title()
age = int(input("How old are you? "))
not_had_bday = True if input("Have you had your birthday yet? (y/n) ") == 'n' else False

# calculate birthyear considering whether they've had their birthday or not
birthyear = date.today().year - age - not_had_bday

print(f"Hi {name}, you are {age} years old, you were born in {birthyear}")