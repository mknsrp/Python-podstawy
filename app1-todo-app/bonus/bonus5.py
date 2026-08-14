waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
for index, item in enumerate(waiting_list):
    print(f"{index + 1}.{item.capitalize()}")


mylist = ['b', 'c', 'd']
mylist.sort(reverse=True)
print(mylist)

names = ['jacek', 'maciek', 'monika', 'sebastian', 'damian']
for i, j in enumerate(names):
    print(f"{i+1}-{j.capitalize()}")