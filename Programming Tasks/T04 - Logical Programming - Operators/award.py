#ask the user for their swim, cycling and running time. Save each one in separate variables.
#sum up all three times to work out the total time
#create an if-elif-else statement to check the total time against the criteria

swimming_time = int(input("What is your swim time in minutes?: "))
cycling_time = int(input("What is your cycling time in minutes?: "))
running_time = int(input("What is your running time in minutes?: "))

total_time = swimming_time + cycling_time + running_time

if total_time <= 100:
    print("Within the qualifying time.Your award is: Provincial Colors")
elif total_time > 100 and total_time <= 105:
    print("Within 5 minutes of the qualifying time. Your award is: Provincial Half Colors")
elif total_time > 105 and total_time <= 110:
    print("Within 10 minutes of the qualifying time. Your award is: Provincial Scroll.")
else:
    print("More than 10 off minutes from the qualifying time. You do not qualify for an award.")