nums = [1, 1, 2, 3,3 ]
uniques= []
for num in nums:
    if num not in uniques:
        uniques.append(num)
print(uniques)