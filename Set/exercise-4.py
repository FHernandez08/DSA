# Update the first set with items that don't exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)

## Notes => the difference_update method can remove any elements from two sets that aren't in each other by comparing sets