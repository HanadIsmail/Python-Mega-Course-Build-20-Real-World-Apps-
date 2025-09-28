'''menu = ["pasta", "pizza", "salad"]

user_choice =int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)


#fixed Bug One

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")

'''
#fixed Bug Two

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")
