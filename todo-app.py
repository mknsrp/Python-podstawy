while True:
    # Get user input and remove space chars form it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        # Check if user action is "add"
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        # Check if user action is "show"
        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}-{item}")

        # Check if user action is "edit"
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        # Check if user action is "complete"
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
            
        # Check if user action is "exit"
        case 'exit':
            break
print("See ya!")


