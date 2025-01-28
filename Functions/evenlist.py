#Write a function that takes a list as input and returns a new list containing only even numbers.

def evenlist(nums):
    evens= []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    print(evens)

evenlist([2,3,4,56,9, 111776])