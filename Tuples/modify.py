numbers = (1, 2,3)
# Convert the tuple into a list to be able to change it
nums= [1, 2, 3]
nums[1] = 5
numbers = tuple(nums)
print(numbers)