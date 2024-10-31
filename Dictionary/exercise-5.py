# Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = dict()

for key in keys:
    new_dict.update({key: sample_dict[key]})

print(new_dict)

## Notes
## Use the update method to add the value pair to the new dictionary (key: sample_dict[key])
## Key-value pair: Key: sample_dict[key] => ie name: Kelly