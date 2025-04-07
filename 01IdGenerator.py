# ID Generator
import random

print("Unique ID generator system")
first_name = (input("What is your first name? "))[0:2].upper()
last_name = (input("What is your last name? "))[0:2].upper()
birth_year = (input("What is your year of birth? YYYY" ))[2:4]
number = random.randint(1000, 9999)

uniqueID = f'{first_name}{last_name}{birth_year}{number}'

print(f"Your unique ID is: {uniqueID}")