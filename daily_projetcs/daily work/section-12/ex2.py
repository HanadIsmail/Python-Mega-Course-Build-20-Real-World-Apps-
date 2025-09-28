def strength(password):
    result =[]
    if len(password)  >= 8:
        result['length'] = True
    else:
        result['length'] = False

    upper_case = False
    digit = False


    for i in password:
        if i.isupper():
            upper_case = True
            result[upper_case] = True

    for i in password:
        if i.isdigit():
            digit = True
            result[digit] = True

    if all(result.Values()):
        return 'strong password'
    else:
        return 'weak password'







