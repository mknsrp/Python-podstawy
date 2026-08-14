contents = ["Siema to jakis krociutki tekst na potrzebe nauki",
            "Siema to drugi tekst na potrzebe nauki",
            "Siema to trzeci tekst"]

filenames = ["pierwszy.txt", "drugi.txt", "trzeci.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../bonus6/{filename}", 'w')
    file.write(content)



