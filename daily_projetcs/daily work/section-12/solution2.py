# Define a function named strength that takes one parameter, password
def strength(password):
    # Create an empty dictionary to store the strength attributes
    result = {}

    # Check the length of the password
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    # Check if the password contains a digit and an uppercase letter
    digit = False
    uppercase = False

    # Iterate over each character in the password
    for i in password:
        # Check if the character is a digit
        if i.isdigit():
            digit = True
        # Check if the character is an uppercase letter
        if i.isupper():
            uppercase = True

    # Store the results in the dictionary
    result["digits"] = digit
    result["upper-case"] = uppercase

    # Check if all the strength attributes are True
    if all(result.values()):
        # Return "Strong Password" if all attributes are True
        return "Strong Password"
    else:
        # Return "Weak Password" if any attribute is False
        return "Weak Password"