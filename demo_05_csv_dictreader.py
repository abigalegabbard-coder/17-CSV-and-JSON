import csv

filepath = "employees.csv"

with open(filepath, "r", newline = "") as file:
    content = csv.DictReader(file) #Loads everything as a csv reader object
    #print(content)

    #for line in content:
    #    print(line)
    #    print(line["Name"]) #access a specific field of the csv

    # Print the info with line numbers:
    for line_num, line in enumerate(content, start = 2):
        print(f"{line_num}: {line}")