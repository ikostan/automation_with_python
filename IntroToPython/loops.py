my_variable = "hello"

# print first letter only
print(my_variable[0])

for l in my_variable:
    print(l, end='')  # print all letters on the same line

print()

for n, l in enumerate(my_variable):
    if n % 2 == 0:
        print(l, end="")
    else:
        print(" ", end="")

print()

for n, l in enumerate(my_variable):
    if n % 2 != 0:
        print(l, end="")
    else:
        print(" ", end="")

num_list = [1, 2, 2, 6, 8, 9, 0]
for number in num_list:
    print(number ** 2)


is_true = True
n = 0
while is_true:
    print("Still true")
    n += 1
    if n > 10:
        print("Stop printing")
        break

while is_true:
    print("HaHa")
    user_input = input("Should we print again? (y/n)")
    if user_input.lower() == "n":
        is_true = False
        print("Stop printing")
