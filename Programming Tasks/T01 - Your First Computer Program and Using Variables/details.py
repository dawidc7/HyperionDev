#ask the user for their name (ask for input)
#ask the user for their age (ask for input)
#ask the user for their house number (ask for input)
#ask the user for their street name (ask for input)
#output string containing all of the above in an f string

user_name = input("What is your name?")
user_age = input("What is your age?")
house_num = input("What is your house number?")
user_street = input("What is your street name?")

print(f"This is {user_name}. He is {user_age} years old \n\
and lives at house number {house_num} on {user_street}")