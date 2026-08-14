import csv

with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

while True:
    city = input("Enter a city: ")

    for row in data[1:]:
        if row[0] == city:
            print(row[1])
