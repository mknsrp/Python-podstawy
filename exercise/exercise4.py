# filenames = ["exercise4-data/a.txt", "exercise4-data/b.txt", "exercise4-data/c.txt"]
#
# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.readline()
#     print(content)
#
# file = open('file.txt', 'w')
# file.write('Siema')
# file.close()


file = open('exercise4-data/a.txt','r')
content = file.readlines()
for x in content:
    print(x.strip().split())