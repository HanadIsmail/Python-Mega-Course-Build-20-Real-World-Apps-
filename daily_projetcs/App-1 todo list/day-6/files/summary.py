todos = []

while True:
    user_action = input("Type, add, show, edit, delete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + '\n'

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, items in enumerate(todos):
                item = items.strip('\n')
                row = f"{index +1}-{item.capitalize()}"
                print(row)

        case "edit":
            number = int(input("Enter a number to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case "delete":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number = int(input("enter a number to delete: "))
            number = number - 1
            todos.pop(number)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "exit":
            print("Thank you for using this program")
            break

print("Bye!")