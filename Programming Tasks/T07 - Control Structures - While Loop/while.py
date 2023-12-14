#declare variables and assign them initial values of 0
total = 0
num_count = 0
user_num = 0

#while loop to run until user input is -1
while user_num != -1:
    user_num = int(input("Please enter a num: "))
    total += user_num # sums up total for later calculation
    num_count += 1 # keeps track of amount of numbers entered

print(total / (num_count - 1)) #num_count is decreased by 1 because the while loop is to not include the instance of -1