# python weight converter

while True: # start an infinite loop 
    try:
        weight = float(input("Enter weight: ")) # get user input for weight
    except ValueError: # handle the case where the user enters a non-numeric value
        print("Invalid input! Please enter a numeric value for weight.") 
        continue
    while True: # start another infinite loop for unit input
        unit = input("Enter unit (kg or lb): ") # get user input for unit    
        if unit.lower() == "kg":
            converted_weight = weight * 2.2  # Convert kg to lb
            print(f"{weight} kg is equal to {converted_weight:.1f} lb") # round to 1 decimal place
            break
        elif unit.lower() == "lb":
            converted_weight = weight / 2.2  # Convert lb to kg
            print(f"{weight} lb is equal to {converted_weight:.1f} kg")# round to 1 decimal place
            break
        else:
            print("Invalid unit! Please enter 'kg' or 'lb'.") # handle the case where the user enters an invalid unit
    break  # exit the outer loop after a successful conversion