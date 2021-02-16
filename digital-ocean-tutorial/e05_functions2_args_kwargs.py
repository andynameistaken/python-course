# order of everyting in function:
'''
def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
... stuff

'''

def multiply(x, y):
    print(x * y)


def multiply_args(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


def print_kwargs(**kwargs):
    print(kwargs)


def print_values(**kwargs):
    for k, v in kwargs.items():
        print("The value of {} is {}".format(k, v))


def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)


def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)


def main():
    multiply(2, 2)
    multiply_args(2, 3, 4)
    print_kwargs(
        kwargs_1="Shark",
        kwargs_2=4.5,
        kwargs_3=True
    )
    print_values(my_name="Sammy", your_name="Casey")
    # *args work with tuples
    args = ("Sammy", "Casey", "Alex")
    some_args(*args)
    # and lists
    my_list = [2, 3]
    print("with *")
    some_args(1, *my_list)

    # kwargs as argument
    kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
    some_kwargs(**kwargs)


if __name__ == '__main__':
    main()
