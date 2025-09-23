filenames = ["exercise4-data/a.txt", "exercise4-data/b.txt", "exercise4-data/c.txt"]

for filename in filenames:
    file = open(filename, 'r')
    content = file.readline()
    print(content)


