# Remove items from the set at once
set1 = {10, 20, 30, 40, 50}

set1.difference_update({10, 20, 30})
print(set1)

## Notes => difference_update method will remove elements from a set by using the items added, removing them, and returning a new set with the updated values