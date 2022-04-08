from functools import wraps

def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

@decorator
def say():
    print("Hello world")

say()
