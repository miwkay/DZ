from functools import wraps


def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner


@decorator
def say():
    print("Hello world")


say()
