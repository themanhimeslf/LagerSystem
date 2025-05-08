import json

# Define the data as a Python dictionary
data = {
    'name': 'Bob',
    'age': '25',
    'city': 'Los Angeles'
}

# Write data to a JSON file
with open('output.json', 'a') as f:
    json.dump(data, f)

#a
#w sletter og fjerner

with open('output.json') as f:
    modified_data = json.load(f)
    print('Modified data:', modified_data)