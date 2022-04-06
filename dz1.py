def decorator(func):
    def inner():
        func()
    return inner

@decorator
def say():
    print("Hello world")

say = say()
say

