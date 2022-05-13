from types import MethodType


class StaticMethod:

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

    def __call__(self, *args, **kwds):
        return self.f(*args, **kwds)


class Terra:
    @staticmethod
    def luna(price):
        if price > 0.01:
            print("The 'Luna' will live..")
        else:
            print("..still belive!")


class ClassMethod:

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        if hasattr(type(self.f), '__get__'):
            return self.f.__get__(cls, cls)
        return MethodType(self.f, cls)

class ScamYear:
    @classmethod
    def luna(cls, x):
        print(f"{x} is scam of the year!")


Terra.luna(0.0001)
ScamYear.luna("Luna")
