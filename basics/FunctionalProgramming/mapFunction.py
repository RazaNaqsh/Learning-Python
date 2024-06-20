#  map(action, data)

my_list = [1, 2, 3]


def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, my_list)))

# This map function does not modify the my_list , it returns a new list
