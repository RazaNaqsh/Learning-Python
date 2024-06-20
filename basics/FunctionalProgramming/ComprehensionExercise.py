some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


# do the above using list comprehension

my_list = list(set([char for char in some_list if some_list.count(char) > 1]))

print(my_list)
