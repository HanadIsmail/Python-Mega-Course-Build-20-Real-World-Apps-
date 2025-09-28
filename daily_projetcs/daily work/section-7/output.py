
while True:
    user = input("type add show edit delete exit : ")
    user.strip()

    match user:
        case 'add':
            todo = input("Enter a todo : ") + '\n'

            file = open('xogta7.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('xogta7.txt','w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('xogta7.txt','r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate (todos):
                item = item.strip('\n')
                row= f"{index +1}: {item}"
                print(row)
        case 'edit':
            number = int(input("Enter number to edit : "))
            number = number -1
            new_todo= input("enter new todo")
            todos[number] = new_todo
        case 'delete':
            number = int(input("Enter number to delete : "))
            todos.pop(number-1)
        case 'exit':
            break


