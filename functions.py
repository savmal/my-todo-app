import os

FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items.
    """
    todos_local = ''
    try:
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
    except FileNotFoundError:
        print(f"File {filepath} Not Found")
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write list of to-do items in a text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())