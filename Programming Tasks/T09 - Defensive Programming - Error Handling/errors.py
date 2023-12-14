# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")   #Syntax Error, the parentheses were missing
print("\n")     #Syntax Error because of the missing parentheses and wrong indent

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"   #Runtime Error, because of unnecessary indent and the wrong operator used. Instead of == use =
age = int(age_Str)         #Runtime error because the code is trying to change the whole string to an int which is not possible,
                           #age_Str value changed to just 24
print("I'm " + str(age) + " years old.") #Runtime Error, age has to be changed into a string before concatenating in a string

    # Variables declaring additional years and printing the total years of age
years_from_now = 3
total_years = age + years_from_now  #Runtime Error because years_from_now is a string. Removed quotation marks.

print("The total number of years:" + str(total_years))    #Syntax Error because of missing parentheses and Logical error because the program
                                                        # is trying to concatenate a variable (which also doesn't exist and would cause a
                                                        # Syntax Error) which is in quotation marks. Got rid of quotation marks and changed the variable 
                                                        # to str(total_years)
# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12   #Runtime error because the variable total hasn't been defined and so holds no value. Changed to total_years.
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")   #Syntax Error because of missing parentheses and Logical error
                                                                                     # because of the missing addition of 6 months.

#HINT, 330 months is the correct answer

