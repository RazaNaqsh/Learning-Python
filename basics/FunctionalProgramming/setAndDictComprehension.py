# Same as list comprehension but just the change in bracket
my_list2 = {char for char in "hello"}

print(my_list2)

my_list3 = {num for num in range(0, 10)}

print(my_list3)

# The first var can be an expression
my_list4 = {num * 2 for num in range(0, 10)}
print(my_list4)


# Dictionary comprehension

simple_dict = {"a": 1, "b": 2}


my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}


print(my_dict)


# Example two
my_dict2 = {num: num**2 for num in [1, 2, 3]}

print(my_dict2)
