

# 3. Use the Module in Another Python Script:

# You can now use the functions and variables 
# defined in your module in other Python scripts by importing the module.

# pgm.py

import mod

mod.greet("Alice")  # Output: Hello, Alice!

result = mod.add_numbers(5, 3)
print(result)  # Output: 8

print(mod.PI)  # Output: 3.14159

print(mod.__doc__)
print(mod.greet.__doc__)