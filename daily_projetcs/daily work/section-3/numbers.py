todos= []

while True:
    user = input("Type add , show, exit: ")
    user = user.strip()

    match user:
        case 'add':
            todo = input("Enter a to do:")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            print("Existing....")
            break
print("bye!")

