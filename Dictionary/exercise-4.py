# Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict = dict.fromkeys(employees, defaults)
print(new_dict)

## Notes
## Uses fromkeys to add the same values to each pair