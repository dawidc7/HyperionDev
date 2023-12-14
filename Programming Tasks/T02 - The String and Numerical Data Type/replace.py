#save the test string in a variable
#replace every instance of ! with a blank space using replace() and save to a new variable
#print using a print statement and use .upper to make every character a capital
#use string slicing to print the string in reverse. using -1 as the step.

original_string = "The!quick!brown!fox!jumps!over!the!lazy!dog"
new_string = original_string.replace("!", " ")
print(new_string.upper())
print(new_string[::-1])