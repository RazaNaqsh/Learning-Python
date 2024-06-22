# print(list(range(10)))


def generator_function(num):
    for i in range(num):
        yield i * 2  # yield keyword pauses the function


# for item in generator_function(100):
#     print(item)

# What this does is that it just returns
# a single i from the generator, and doesnt store the whole in the memory


g = generator_function(10)
print(g)  # a generator object, which is an iterable

# next keyword
next(g)
next(g)
print(next(g))

# next(g) gives the next iterable, for eg first time its 0*2, then 1*2,
# then third time its 2*2 thus we get 4 output on line 22

# But the next shud not exceed the range , like if range given is 10,
# we cant call next 11 times

# for i in g:  # thus we iterate over the g to print the numbers
#     print(i)
