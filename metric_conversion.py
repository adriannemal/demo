# Define function to convert meters to feet
def meter_to_foot(meter):
    return meter * 3.281 

# Define function to convert feet to meters
def foot_to_meter(foot):
    return foot * 0.305

# Prompt the user to choose a conversion calculator
type_of_conversion = int(input(""" Which conversion calculator would you like to use? Please enter 1 or 2 
                        1. Meter to foot
                        2. Foot to meter
                        """))

# Check the user's choice and perform the corresponding conversion  
if type_of_conversion == 1:
# If the user chooses 1, convert from meters to feet

    meter = float(input("Please enter the length in meters: "))
    foot_calculation = meter_to_foot(meter)
    print(f"You have entered {meter} meters.\
    This is {foot_calculation} feet.")

 # If the user chooses 2, convert from feet to meters
elif type_of_conversion == 2:
    
    foot = float(input("Please enter the length in feet: "))
    meter_calculation = foot_to_meter(foot)
    print(f"You have entered {foot} feet.\
    This is {meter_calculation} meters.")

# If the user enters an invalid number, prompt them to enter a valid number
else:
    print(" Please enter a valid number:")

