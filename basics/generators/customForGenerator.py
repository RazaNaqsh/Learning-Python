def special_for(iterable):
    iterator = iter(
        iterable
    )  # to create a custom iterable object which we can iterate over
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])
