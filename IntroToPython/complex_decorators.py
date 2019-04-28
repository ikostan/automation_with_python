import functools


def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_function(*args, **kwargs):
            print("In the decorator")
            if number == 56:
                print("Not running the function")
            else:
                func(*args, **kwargs)
            print("After the decorator")
        return function_that_runs_function
    return my_decorator


@decorator_with_arguments(57)
def my_function_foo(x, y):
    print(x + y)


my_function_foo(56, 67)

