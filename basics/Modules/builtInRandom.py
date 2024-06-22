import random

print(random.randint(1, 10))
print(random.random())

my_list = [1, 2, 3, 4, 5]

random.shuffle(my_list)

print(my_list)

print(random.choice([1, 2, 3, 4]))
