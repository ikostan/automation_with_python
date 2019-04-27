class Student:
    def __init__(self, name: str, school: str):
        self.name = name.capitalize()
        self.school = school.capitalize()
        self.marks = []

    def average_mark(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name: str, salary: float):
        # return a new student called 'friend_name' in the same school as self.
        return cls(friend_name, origin.school, salary)


class WorkingStudent(Student):
    def __init__(self, name: str, school: str, salary: float):
        super().__init__(name, school)
        self.salary = salary


try:
    anna = WorkingStudent('anna', "Oxford", 1800.0)
    print(anna.salary)

    friend = WorkingStudent.friend(anna, 'greg', 800.0)
    print(friend.name)
    print(friend.school)
    print(friend.salary)
except AttributeError as err:
    print("{0}".format(err))
except TypeError as err:
    print("{0}".format(err))


