filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"exercise3-data/{filename}", 'w')
    file.write('Hello')
    file.close()