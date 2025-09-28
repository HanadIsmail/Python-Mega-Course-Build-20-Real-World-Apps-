def water_state(temperature):
    if temperature <= 0:
        return 'solid'
    elif 0 < temperature > 100:
        return 'liquid'
    else:
        return 'Gas'
