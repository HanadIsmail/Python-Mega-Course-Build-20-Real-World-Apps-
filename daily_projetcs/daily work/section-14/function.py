def get_todos(filepath = "todos14.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()

    return todos


def write_todos(todos, filepath = 'todos13.txt'):
    with open('todos14.txt', 'w') as file:
        file.writelines(todos)