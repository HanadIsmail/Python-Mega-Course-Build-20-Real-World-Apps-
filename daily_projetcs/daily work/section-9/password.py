password = input("Enter your password: ")

result= {}

if len(password) >= 8:
    result["Lenght"] = True
else:
    result["Lenght"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppwer-case"] = uppercase

print(result)

if all(result.values()):
    print("strong password")
else:
    print("weak password")






