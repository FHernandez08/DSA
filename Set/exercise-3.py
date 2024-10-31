# Get only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_set = set1.union(set2)
print(unique_set)

## Notes => the union() method will combine the two sets while removing the duplicate elements