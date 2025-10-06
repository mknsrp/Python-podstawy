# while True:
#     print("Hello")

#
# user_prompt = "Enter a todo: "
#
# todos = []
# while True:
#     todo = input(user_prompt)
#     print(todo.title())
#     todos.append(todo)
#


# fruits = {"banana": 3, "lichi": 5, "coconut": 1}
# print(fruits["banana"])
try:
    mylist =[1, 2, 3]
    print(mylist[3])
except IndexError:
    print("Your index is out of range.")