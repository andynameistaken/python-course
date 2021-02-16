def function_name(argument, argument1):
    """This is example function, which ironically does't have any purpose, but it will
    teach you something anyway"""
    argument += 1
    argument1 += 1
    print(argument, argument1)


var = 1


def function1():
    global var
    var = 2


def append_element(lst: list):
    """this function appends 1 to a list"""
    lst.append(1)
    print(lst)


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        # print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


# def default_val_function(number: int = 4, string):   optional arguments always firs!
#     ...


def default_val_function(string: str, number: int = 4):
    print(string, number)


var1 = 5


def in_defining_scope(arg=var1):
    print(var1)


def append_to_list(a, L=[]):
    """Important warning: The default value is evaluated only once. This makes a difference when
    the default is a mutable object such as a list, dictionary, or instances of most classes."""
    L.append(a)
    return L

def append_to_list2(a, L = None):
    """
    If you don’t want the default to be shared between subsequent calls,
    you can write the function like this instead:
    """
    if L is None:
        L = []
    L.append(a)
    return L



def main():
    # x = y = 1
    # print(x, y)
    # x += 1
    # print(x, y)
    # function_name(x, y)
    # print(x, y)
    # print(function_name.__doc__)
    lis = [2, 2, 3]
    # append_element(lis)
    # print(lis)
    # print(var)
    # function1()
    # print(var)
    # a, b = 0, 1
    # # print(a, b)
    # a, b = b, a + b
    # print(a, b)
    #
    # # function fib
    # print(fib)
    # f = fib
    # f(100)
    #
    # # function fib2
    # f100 = fib2(100)  # call it
    # f100  # write the result
    #
    # # Default functions
    # default_val_function("hello", 300)
    # default_val_function("Hello")

    # --The default values are evaluated at the point of function definition in the defining scope--
    var1 = 300
    in_defining_scope()

    # print(append_element.__doc__)
    print(append_to_list(1))
    print(append_to_list(2))
    print(append_to_list(3))

    print(append_to_list2(1))
    print(append_to_list2(2))
    print(append_to_list2(3))



    """
    What does if __name__ == “__main__”: do?
        When the Python interpreter reads a source file, it executes all of the code found in it.
        Before executing the code, it will define a few special variables. For example, if the python interpreter is
         running that module (the source file) as the main program, it sets the special __name__ variable to have 
         a value "__main__". If this file is being imported from another module, __name__ will be set 
         to the module's name.
        In the case of your script, let's assume that it's executing as the main function, e.g. something like
        python threading_example.py
        on the command line. After setting up the special variables, it will execute the import statement and load 
        those modules. It will then evaluate the def block, creating a function object and creating a variable called
         myfunction that points to the function object. It will then read the if statement and see that __name__ does 
         equal "__main__", so it will execute the block shown there.
        One reason for doing this is that sometimes you write a module (a .py file) where it can be executed directly. 
        Alternatively, it can also be imported and used in another module. By doing the main check, you can have that 
        code only execute when you want to run the module as a program and not have it execute when someone just wants 
        to import your module and call your functions themselves.
    """


if __name__ == '__main__':
    main()
