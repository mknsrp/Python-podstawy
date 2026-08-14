# filenames = ["1.doc", "1.report", "3.presentation"]

# for file in filenames:
#     file = file.replace('.', '-', 1)
#     print(f"{file}.txt")

# filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
# print(filenames)


numbers = [1, 2, 3, 4, 5, 6]

odd = [number for number in numbers if number % 2 != 0]
print(odd)
