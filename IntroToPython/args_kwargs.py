def my_method(arg1, arg2):
    return arg1 + arg2


def my_long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5


def my_list_addition(list_args: list):
    return sum(list_args)


def addition_simplified(*args):
    return sum(args)


def addition_kwads(*args, **kwargs):
    print(args)
    print(kwargs)


print(my_method(5, 6))
print(my_long_method(5, 6, 20, 70, 48))
print(my_list_addition([5, 6, 20, 70, 48]))
print(addition_simplified(5, 6, 20, 70, 48))
addition_kwads(12, 34, 56, name='Jose', location='UK')
