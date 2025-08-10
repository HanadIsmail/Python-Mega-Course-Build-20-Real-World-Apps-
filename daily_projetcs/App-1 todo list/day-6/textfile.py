
while True:
    user = input("Type add, show,edit,delete,or exit: ")
    user.strip()

    match user:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt","w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index,item in enumerate(todos):
                row = f"{index +1}:{item}"
                print(row)

        case "delete":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            number= int (input("Enter a number to delete:"))
            number = number -1
            todos.pop(number)

            file = open("todos.txt","w")
            file.writelines(todos)
            file.close()

        case "exit":
            break