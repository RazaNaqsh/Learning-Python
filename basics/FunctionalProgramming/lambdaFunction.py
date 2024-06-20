from functools import reduce

# my_list = [1, 2, 3]

# # This lambda function is not stored anywhere, but just used once
# # One time anonymous function

# # Syntax:
# # lambda param : action(param)
# print(list(map(lambda item: item * 2, my_list)))


# # Filter using lambda function
# # Odd numbers only
# print(list(filter(lambda item: item % 2 != 0, my_list)))

# # Reduce using lambda
# # reduce(function, data,starting point)
# print(reduce(lambda acc, item: acc + item, my_list, 10))


# # Exercise
# # Print squared list

# print(list(map(lambda item: item**2, my_list)))


# List sorting acc to 2nd element

a = [(0, 2), (4, 3), (10, -1), (9, 9)]

# If we simply sort a

a.sort()  # sorts on the basis of first key
print(a)


# Sorting on the basis of 2nd key

a.sort(key=lambda x: x[1])

print(a)
