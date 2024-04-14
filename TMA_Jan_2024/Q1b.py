# prompt the user for time input in 24 hour format
time = input("Enter time in 24-hour format: ")

# displays a greeting with the time in 12-hour format
if int(time) >= 0000 and int(time) <= 1159:
    if int(time) <= 100:
        print("Good morning! Time is {}.{}am".format(int(time[0:2])+12, time[2:4]))
    else:
        print("Good morning! Time is {}.{}am".format(time[0:2], time[2:4]))
elif int(time) >=1200 and int(time) <= 1759:
    if int(time) <= 1300:
        print("Good afternoon! Time is {}.{}pm".format(time[0:2], time[2:4]))
    else:
        print("Good afternoon! Time is {}.{}pm".format(int(time[0:2])-12, time[2:4]))
else:
    print("Good evening! Time is {}.{}pm".format(int(time[0:2])-12, time[2:4]))