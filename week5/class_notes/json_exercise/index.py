import json
# from faker import Faker

# fake = Faker()

with open('file.json', 'r') as f:
    family = json.load(f)

print("janes children: ")

for child in family['children']:
    for key, value in child.items():
        print(f"my{key} is {value}")

# with open()
