#ask the user for a string and save it to a variable #find the length of the string using len and print it
#find the last character in a string using negative indexing and replace every instance with "@" #print the last three characters of a string by using negative indexing and finding the length #of the string - 4
#print the first three and last 2 characters of a string together by using indexing to find #the first three and the length of the string - 2 and negative index to find the last 2. Print this in a #f string for easy formatting
10
11
12
13
14
15
str_manip = input("Please write a sentence: ")
print(len(str_manip))
print(str_manip.replace(str_manip[-1], "@"))
print(str_manip[: (len (str_manip) - 4):-1])
print(f"{str_manip[0:3]}{str_manip[(len(str_manip) - 2):len(str_manip)]}")