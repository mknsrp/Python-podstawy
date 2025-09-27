while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "show"
    if 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    # Check if user action is "edit"
    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    # Check if user action is "complete"
    if 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        removed_todo = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {removed_todo} was removed form the list."
        print(message)
    # Check if user action is "exit"
    if 'exit' in user_action:
        break
print("See ya!")


