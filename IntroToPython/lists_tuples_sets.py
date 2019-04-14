my_variable = "hello"

grade_one = 77
grade_two = 80
grade_three = 90

# print((grade_one + grade_two + grade_three) / 3)

grade_four = 95
grade_five = 100

grades_list = [grade_one, grade_two, grade_three, grade_four, grade_five]
grades_tuple = (grade_four, grade_five, grade_one, grade_two, grade_three)
grades_set = {77, 80, 90, 100, 100}

print(sum(grades_list) / len(grades_list))
grades_list.append(73)
print(sum(grades_list) / len(grades_list))
print(grades_set)
print(sorted(grades_tuple))

grades_tuple = grades_tuple + (66,)
print(grades_tuple)
print(sum(grades_tuple) / len(grades_tuple))

for i in range(len(grades_set)):
    print(grades_set.pop())

print(grades_set)

for i, b in enumerate(grades_tuple):
    print("{0}: {1}".format(i, b))

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 4, 7, 9, 11}

print("Intersection: {0}".format(your_lottery_numbers.intersection(winning_numbers)))
print("Union: {0}".format(your_lottery_numbers.union(winning_numbers)))
print("Intersection: {0}".format(your_lottery_numbers.difference(winning_numbers)))


