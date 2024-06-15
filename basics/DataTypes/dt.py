# Lists

# The most basic way to initialize list is
my_list = [1,2,3,4,5]

# It has its own methods
# append
# insert , has two params
# pop
# remove
# count
# reverse
# and more you can search from docs
my_list.append(6)
my_list.remove(6)
print(my_list)

# Using range to define list
range_list = list(range(1,10))
print(range_list)



# Tuples are similar to lists but they are immutable meaning we cant change them
my_tuple = ('a','b','c','d')

# Then theres dictionary, where we define data in key value pairs
my_dict = {
   'name':'raza',
   'age':21,
   'status':'studying'
}

print(my_dict['name'])

# Also set, where there is no duplicate data, each data element is unique, and it has set like operations like in math
my_set = {1,2,3,4,5,5,5}

print(my_set)
# outputs only unique values, 5 is only printed once