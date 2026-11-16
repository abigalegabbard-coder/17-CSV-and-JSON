import csv

filepath = "employees.csv"

with open(filepath, "r", newline = "") as file:
    content = csv.reader(file) #Loads everything as a csv reader object
    #print(content)
    # Skip the header row:
    next(content)
    for line in content:
        print(line)
        print(line[0]) #access a specific field of the csv