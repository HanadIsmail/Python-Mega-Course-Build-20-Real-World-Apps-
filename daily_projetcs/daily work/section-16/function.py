def get_todos(filepath = "../section-15/todos15.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()

    return todos


def write_todos(todos, filepath = 'todos13.txt'):
    with open('../section-15/todos15.txt', 'w') as file:
        file.writelines(todos)

