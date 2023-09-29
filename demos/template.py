#!/usr/bin/env python3

"""
this script is a general template script 
"""

__author__ = 'Fenna Feenstra'
__version__ = '1.0'

## code

# imports
import sys

# constants
# functions
# main
def main(args):
    if len(args) < 2:
        print(len(args))
        print('please provide a datapath')
    else:
        path = args[1]
        print(path) 
    #prep
    #work
    #finalize

    return 0


if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)