"""
Imports practice
Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use
that in your script of choice.
"""

from mod_dir.module1 import test_function_mod1 as f1, test_function_mod2 as f2

print(f1(), f2())
