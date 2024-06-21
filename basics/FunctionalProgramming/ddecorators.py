# Decorators are wrappers that make the functions super powered
# with extra functionalities
# Decorator
def my_decorator(func):
    def wrap_func():
        print("*****")
        func()
        print("*****")

    return wrap_func


@my_decorator
def hello():
    print("helloo")


# hello()

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i * 5


long_time()
