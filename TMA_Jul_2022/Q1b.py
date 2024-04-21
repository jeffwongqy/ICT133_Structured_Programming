# prompt the user for height measurement
height_measurement = float(input("Enter height measurement (cm): "))
# prompt the user for chest measurement
chest_measurement = float(input("Enter chest measurement (cm): "))
# prompt the user for waist measurement
waist_measurement = float(input("Enter waist measurement (cm): "))


# find the t-shirt size based on the chest measurement 
if chest_measurement >= 128:
    chest_tshirt_size = 8
elif chest_measurement >= 120 and chest_measurement < 128:
    chest_tshirt_size = 7
elif chest_measurement >= 112 and chest_measurement < 120:
    chest_tshirt_size = 6
elif chest_measurement >= 104 and chest_measurement < 112:
    chest_tshirt_size = 5
elif chest_measurement >= 96 and chest_measurement < 104:
    chest_tshirt_size = 4
elif chest_measurement >= 88 and chest_measurement < 96:
    chest_tshirt_size = 3
elif chest_measurement >= 80 and chest_measurement < 88:
    chest_tshirt_size = 2 
else:
    chest_tshirt_size = 1

# find the t-shirt size based on the height measurement 
if height_measurement >= 185:
    height_tshirt_size = 8
elif height_measurement >= 180 and height_measurement < 185:
    height_tshirt_size = 7
elif height_measurement >= 175 and height_measurement < 180:
    height_tshirt_size = 6
elif height_measurement >= 170 and height_measurement < 175:
    height_tshirt_size = 5
elif height_measurement >= 165 and height_measurement < 170:
    height_tshirt_size = 4
elif height_measurement >= 160 and height_measurement < 165:
    height_tshirt_size = 3
elif height_measurement >= 155 and height_measurement < 160:
    height_tshirt_size = 2
else:
    height_tshirt_size = 1

# find the t-shirt size based on the waist measurement 
if waist_measurement >= 116: 
    waist_tshirt_size = 8
elif waist_measurement >= 108 and waist_measurement < 116:
    waist_tshirt_size = 7
elif waist_measurement >= 100 and waist_measurement < 108:
    waist_tshirt_size = 6
elif waist_measurement >= 92 and waist_measurement < 100:
    waist_tshirt_size = 5
elif waist_measurement >= 84 and waist_measurement < 92:
    waist_tshirt_size = 4
elif waist_measurement >= 76 and waist_measurement < 84:
    waist_tshirt_size = 3
elif waist_measurement >= 70 and waist_measurement < 76:
    waist_tshirt_size = 2
else:
    waist_tshirt_size = 1

# recommend the t-shirt size based on the fitting rules
if height_tshirt_size == waist_tshirt_size == chest_tshirt_size:
    fitting_rules_outcome = "best fit"
    recommended_size = height_tshirt_size
elif height_tshirt_size > chest_tshirt_size and height_tshirt_size > waist_tshirt_size:
    fitting_rules_outcome = "relaxed fit"
    recommended_size = height_tshirt_size
elif chest_tshirt_size > height_tshirt_size and chest_tshirt_size > waist_tshirt_size:
    fitting_rules_outcome = "relaxed fit"
    recommended_size = chest_tshirt_size
elif waist_tshirt_size > height_tshirt_size and waist_tshirt_size > chest_tshirt_size:
    fitting_rules_outcome = "relaxed fit"
    recommended_size = waist_tshirt_size
elif height_tshirt_size > chest_tshirt_size and  waist_tshirt_size > chest_tshirt_size:
    fitting_rules_outcome = "regular fit"
    recommended_size = height_tshirt_size
elif waist_tshirt_size > height_tshirt_size and chest_tshirt_size > height_tshirt_size:
    fitting_rules_outcome = "regular fit"
    recommended_size = waist_tshirt_size
elif height_tshirt_size > waist_tshirt_size and chest_tshirt_size > waist_tshirt_size:
    fitting_rules_outcome = "regular fit"
    recommended_size = chest_tshirt_size

# display the recommendation of the t-shirt size
print("You are size: {} ({})".format(recommended_size, fitting_rules_outcome))