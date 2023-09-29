#!/usr/bin/env python3

"""
module to demonstrate __name__ and __main__
        usage: caller.py <widht> <length>
"""

__author__ = "fennaf"

## CODE
# Imports
import mymodule
import sys

def identity_info():
    print("I am in caller.py now")
    print("__name__: ", __name__)
    return 0

def main(args):
    if len(args) < 3:
        print("please provide width and length argument")
    else:
        identity_info()
        b = mymodule.calculate_area(int(args[1]),int(args[2]))
        print("area", b)
    return 0

if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)





