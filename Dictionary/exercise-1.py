# Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

combined_dict = dict(zip(keys, values))
print(combined_dict)

## Notes
## Zip will combine variables and make it into a tuple to which is turned into a dict