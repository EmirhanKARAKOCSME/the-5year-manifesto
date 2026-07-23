import math

while True:
    try:
        radius = float(input("Enter the radius of the sphere: ")) # get user input for radius
        if radius < 0:
            raise ValueError("Radius cannot be negative.") #prompt user to enter a positive number
    except ValueError as e:
        print(f"Invalid input! Please enter a valid number: {e}") 
        # continue was unnecessary here 
    else:
        volume = 4/3 * math.pi * (radius ** 3) # calculate the volume of the sphere 
        print("The volume of the sphere is:", volume)
        break  # Exit the loop after successful calculation