#Ask user for input and change the input to an int. Save the input in a variable called age
#error proof the code by using a while loop to make sure the age entered is a positive integer
#write if-elif-else statement to check for all the required conditions
#if age is over 100, print statement
#else if age is bigger than or equal to 65, print statement
#else if age is equal to 21, print statement
#else if age is smaller than 13, print statement
#else for any other age, print statement
age = int(input("What is your age?: "))

while age < 0:
    age = int(input("You can't be minus years old, try again: "))

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number")



