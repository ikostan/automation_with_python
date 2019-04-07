# Lesson 1: variables
a = 5
b = 10
my_variable = 56
my_10_variable = 10

string_variable = 'hello'
double_quotes_string = "Hello world"

#print(my_variable)
#print(string_variable)
#print(double_quotes_string)
#print("Hi there")
#print(123)

# Lesson 2: methods


def my_print_method(my_argument=''):
    print("Hello")
    print("World")
    print(my_argument)


#my_print_method()
#my_print_method("hello, world")


def my_multiply_method(number_one, number_two):
    return number_one * number_two


#result = my_multiply_method(5, 3)
#print(result)
#my_print_method(result)
my_print_method(my_multiply_method(5, 3))
