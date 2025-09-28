# Define constants for freezing point and boiling point of water
FREEZING_POINT = 0
BOILING_POINT = 100


# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to the freezing point
    if temperature <= FREEZING_POINT:
        return "Solid"
        # Check if the temperature is between the freezing point and boiling point
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
        # Return "Gas" for all other cases
    else:
        return "Gas" 