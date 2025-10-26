def get_todos(filepath='files/todos.txt'):
    """ Reads a text file and returns the list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath ="files/todos.txt"):
    """ Writes the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())