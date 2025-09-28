import csv

with open('weather.csv' , 'r') as file:
    data = list(csv.reader(file))


city = input("Enter city name: ")

for row in data[1:]:
    if row[0] == city:
        print(f"the weather in {city} is {row[1]}C'" )