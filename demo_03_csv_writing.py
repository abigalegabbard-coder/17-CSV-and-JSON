# csv: Comma Seperated Values
import csv

employees = [
    ["Name", "Age", "Job"],
    ["SpongeBob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

# Write the 2d list to file:
with open("employees.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    # Loop through our 2d list and write each record to file
    for row in employees:
        writer.writerow(row)
    writer.writerow(["Mr. Klins", 99, 'Corpse, Plant food"'])

print(f"CSV file written")

# Write it all at once
with open("employees_2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees) # Pass om the whole 2d list