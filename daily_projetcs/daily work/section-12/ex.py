liter = float ( input("Enter how much liter? "))


def convert(liter):
    cubic_meter = liter / 1000
    return cubic_meter

print(convert(liter))