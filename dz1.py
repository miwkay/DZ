from functools import wraps

def decorator(func):
    @wraps(func)
    def inner():
        func()
    return inner

@decorator
def say():
    print("Hello world")

say()
