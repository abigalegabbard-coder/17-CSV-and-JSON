import json

try:
    with open("many_people.json", "r") as file:
        data = json.load(file)
    print(data)
except FileNotFoundError:
    print("JSON file not found")
except json.decoder.JSONDecodeError:
    print("That JSON file is not legit!")

# Print out Nami and Pirate from data
with open("many_people.json","r") as file:
    data = json.load(file)
print(data[0]["name"] ,data[0]["job"] )

for record in data:
    print(record["name"], record["job"])

# Print out K-Luh's age
print(data[2]["age"])