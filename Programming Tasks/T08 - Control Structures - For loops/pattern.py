#establish the range the for loop should loop until.
for i in range(7):
    if i == 0 or i == 6:
        print("*")
    elif i == 1 or i == 5:
        print("**")                     #since the star pattern is mirrored, i used an or statement to compare 2 different conditions
    elif i == 2 or i == 4:              #so that the amount of stars printed is mirrored directly in the middle
        print("***")
    elif i == 3 or i == 7:
        print("****")