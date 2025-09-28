def foo(temperature):
    if temperature >= 25:
        return 'HOT'
    elif 15 < temperature < 25:
        return 'warm'
    elif temperature < 15:
        return 'cold'


print(foo(25))
