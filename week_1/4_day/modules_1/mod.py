# mod.py



"""
Tips for Creating Modules:

    Keep related functions, classes, and variables together in a module to maintain organization and readability.
    Use a meaningful module name that reflects its purpose and content.
    Document your module using docstrings to provide information about its usage and functionalities.
    Avoid naming your module with the same name as Python standard library modules or built-in functions to prevent conflicts.

"""

def greet(name):
    """
    this is a greet function inside a mod named module
    """

    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

PI = 3.14159


# In the example above, mymodule.py defines a greet() function, 
# an add_numbers() function, and a variable PI.