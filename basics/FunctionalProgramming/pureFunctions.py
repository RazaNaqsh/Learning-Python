# The functions which does not have any side effects
# Meaning it does not influence the outside world


def multiply_by_2(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list


print(multiply_by_2([1, 2, 3]))
