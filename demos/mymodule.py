#!/usr/bin/env python3

"""
module to import. if __name__ == "__main__": piece of code only is True
when the module is not imported but runs as a single (main) script
"""

__author__ = "fennaf"

## CODE
# Imports

def calculate_area(base, height):
    print("__name__: ", __name__)
    return base*height


if __name__ == "__main__":
    print("I am in mymodule.py")
    a = calculate_area(20,100)
    print("area", a)
