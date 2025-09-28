feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    try:

        parts = feet_inches.split(" ")
        feet = float(parts[0])
        inches = float(parts[1])
        meter = feet * 0.3048 + inches * 0.0254
        return meter
    except IndexError:
        print("please enter inches aswell")



result = convert(feet_inches)
print(result)