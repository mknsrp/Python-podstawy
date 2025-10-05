while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # operator boolean: or, and, not
    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "show"
    elif user_action.startswith("show"):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    # Check if user action is "edit"
    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "complete"
    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        removed_todo = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo - {removed_todo} was removed form the list."
        print(message)
    # Check if user action is "exit"
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("See ya!")


