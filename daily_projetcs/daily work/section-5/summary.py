todos = []

while True:
    user_action = input("Type, add, show, edit, delete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)

        case "show":
            for index, items in enumerate(todos):
                row = f"{index +1}-{items.capitalize()}"
                print(row)

        case "edit":
            number = int(input("Enter a number to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case "delete":
            number = int(input("enter a number to delete: "))
            number = number - 1
            todos.pop(number)

        case "exit":
            print("Thank you for using this program")
            break

print("Bye!")