filenames = ["1.Raw_Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

filenames1 = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
print(filenames1)