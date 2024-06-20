my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)


# But theres a cleaner way using list Comprehension

# syntax = param for patam in iterable
my_list2 = [char for char in "hello"]
# explanation , lets create a var as char,
# now do a for loop using char in iterable

print(my_list2)

my_list3 = [num for num in range(0, 10)]

print(my_list3)

# The first var can be an expression
my_list4 = [num * 2 for num in range(0, 10)]
print(my_list4)


# We can add conditions as well, since the first thing is an expression
# Then a loop , then we can add condition

my_list5 = [num**2 for num in range(0, 10) if num % 2 == 0]
print(my_list5)
