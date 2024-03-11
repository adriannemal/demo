def meter_to_foot(meter):
    return meter * 3.281 

def foot_to_meter(foot):
    return foot * 0.305


type_of_conversion = int(input(""" Which conversion calculator would you like to use? Please enter 1 or 2 
                        1. Meter to foot
                        2. Foot to meter
                        """))
    
if type_of_conversion == 1:
    
    meter = float(input("Please enter the length in meters: "))
    foot_calculation = meter_to_foot(meter)
    print(f"You have entered {meter} meters.\
    This is {foot_calculation} feet.")
    
elif type_of_conversion == 2:
    
    foot = float(input("Please enter the length in feet: "))
    meter_calculation = foot_to_meter(foot)
    print(f"You have entered {foot} feet.\
    This is {meter_calculation} meters.")

else ValueError:
    print(" Please enter valid number.")

