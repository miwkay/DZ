import datetime


class Person:
    person_age = 18

    def __init__(self, age):
        self.person_age = age

    def __str__(self):
        return (f"Age: {self.valid_age(self.person_age)} "
                f"Year of birh: {self.year_of_birth(self.person_age)}")

    @classmethod
    def valid_age(cls, age):
        if cls.person_age <= age:
            print('Adult')
        else:
            print('Too young')

    @staticmethod
    def year_of_birth(age):
        date_now = datetime.datetime.now()
        year_birth = date_now.year - age
        print('Year of birh:', year_birth)


person1 = Person(29)
print(person1)  # Output: Adult Year of birth: 1993
person2 = Person(17)
print(person2)  # Output: Too young Year of birth: 2005

print(Person.valid_age(29))  # Output: Adult
print(Person.year_of_birth(17))  # Output: Year of birth: 2005
