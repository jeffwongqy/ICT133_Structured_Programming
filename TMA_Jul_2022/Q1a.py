
# prompt the user for chest measurement
chest_measurement = float(input("Enter chest measurement (cm): "))

# find the t-shirt size based on the chest measurement 
if chest_measurement >= 128:
    tshirt_size = 8
elif chest_measurement >= 120 and chest_measurement < 128:
    tshirt_size = 7
elif chest_measurement >= 112 and chest_measurement < 120:
    tshirt_size = 6
elif chest_measurement >= 104 and chest_measurement < 112:
    tshirt_size = 5
elif chest_measurement >= 96 and chest_measurement < 104:
    tshirt_size = 4
elif chest_measurement >= 88 and chest_measurement < 96:
    tshirt_size = 3
elif chest_measurement >= 80 and chest_measurement < 88:
    tshirt_size = 2 
else:
    tshirt_size = 1

# display the t-shirt size 
print("Your T-Shirt size is {}".format(tshirt_size))