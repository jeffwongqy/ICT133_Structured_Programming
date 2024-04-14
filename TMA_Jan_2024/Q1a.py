



# prompt the user for year of birth 
birth_year = int(input("Enter year of birth: "))

# calculate if the user aged 21 years and above in 2024
age = 2024 - birth_year 

if age >= 21:
    # prompt the user if they do owns more than 1 property
    own_property = input("Do you own more than 1 property: ")

    if own_property.upper() == 'N':
        # prompt the user for the assessable income for year 2022
        assessable_income = int(input("Assessable Income (2022): "))

        if assessable_income <= 34000:
            print("You will receive total $800 ($600 AP Cash + $200 AP Cash Special Payment)")
        elif assessable_income >= 34000 and assessable_income <= 100000:
            print("You will receive total $500 ($350 AP Cash + $150 AP Cash Special Payment)")
        else:
            print("You will receive total $200 ($200 AP Cash)")
    else:
        print("You will receive total $200 ($200 AP Cash)")
else:
    print("You are not eligible for AP package.")