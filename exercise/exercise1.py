# prompt = input("Enter your name: ")
#
# while True:
#     print(prompt.capitalize())
#
#
# while True:
#     name = input("What is your name? ")
#     print(name.capitalize())

word = ""
mylist = []
while word != "exit":
    word = input("Enter word: ")
    mylist.append(word.capitalize())

print(mylist[:-1])