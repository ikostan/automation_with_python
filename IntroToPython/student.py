class Student:
    def __init__(self, name: str, school: str):
        self.name = name.capitalize()
        self.school = school
        self.marks = []

    def average_mark(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        return "I am going to {0}.".format(self.school)

    @classmethod
    def my_profession(cls):
        return "I am a student."

    @staticmethod
    def profession():
        return "Student."


def remove_brackets(word: str):
    new_word = ''
    for c in word:
        if c != '[' and c != ']':
            new_word += c
    return new_word


anna = Student("anna", "MIT")
anna.marks.append(67)
print(remove_brackets("Student name: {0}, marks: {1}".format(anna.name, anna.marks)))
anna.marks.append(85)
print(remove_brackets("Student name: {0}, marks: {1}".format(anna.name, anna.marks)))
print("Average: {0}".format(anna.average_mark()))
print(Student.my_profession() + " " + anna.go_to_school())
print("I am a " + Student.profession())

