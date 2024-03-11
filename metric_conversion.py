def meter_to_foot(meter):
    return meter * 3.281 


meter = float(input("Please enter the length in meters: "))
    
foot = meter_to_foot(meter)

print(f"You have entered {meter} meters.\
    This is {foot} feet.")

