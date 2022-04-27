import datetime


class Person:
    person_age = 18

    @classmethod
    def valid_age(cls, arg):
        if cls.person_age <= arg:
            print('Adult')
        else:
            print('Too young')

    def __init__(self, age):
        self.valid_age = age

    @staticmethod
    def year_of_birth(age):
        year_now = datetime.datetime.now()
        print('Year of birh:', year_now.year - age)


print(Person.valid_age(15))  # Output: Too young
print(Person.year_of_birth(15))  # Output: Year of birth: 2007
