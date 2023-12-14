# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"   #Runtime Error because python is trying to call a variable that hasn't been defined. Adding quotation marks around Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  #Logical Error as attempting to use an f string but missing the f
                                                                                             #Also the last two variables need to swap places

print(full_spec) #Syntax Error, missing parentheses around the full_spec variable

