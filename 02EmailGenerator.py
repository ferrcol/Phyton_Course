# Email generator

print("Email generator")
first_name = (input("What is your first name? ")).lower()
last_name = (input("What is your last name? ")).lower()
company_name = (input("What is your company name? ")).lower()

email= f'{first_name}.{last_name}@{company_name}.com'

print(f"Your email address is: {email}")