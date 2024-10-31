# Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)

## Notes => To combine lists along with sets, best use the update method to make sure that both it gets combined and also it orders the data