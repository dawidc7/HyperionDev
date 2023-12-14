#--------------------------------------------------------------
#Code for every second letter to be capitalized
test_string = input("Enter any string: ")

letter_final_string = ""    #empty string to append items to later

for i, letter in enumerate(test_string):    #enumerate allows me to access the index and the value at that index
    if i % 2 == 0:
        letter_final_string += letter.upper()   #if index is even, letter is capitalized and appended to final string
    else:
        letter_final_string += letter.lower()   #else, it is lower case and appended
    i += 1
print(letter_final_string)

#---------------------------------------------------------------
#Code for every second word to be capitalized

word_final_string = ""  #initialise an empty string to append items from the for loop
test_string = test_string.split()   #splits the user string into separate entities

for i, word in enumerate(test_string):  #enumerate gets the index and value, allowing me to use the % operator and change the value using 'word'
    if i % 2 == 0:
        word_final_string += word.lower()   #if the word is at an even index, it is lower case and appended to the final string
    else:
        word_final_string += (" " + word.upper() + " ") #if not, it is raised to upper case and spaces are added either side
    i += 1

print(word_final_string)
#---------------------------------------------------------------

