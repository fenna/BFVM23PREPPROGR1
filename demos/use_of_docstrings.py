#!/usr/bin/env python3
'''
This module demonstrates the use of docstrings
   usage: ./use_of_docstrings.py your_name

'''
#IMPORTS
import sys


#FUNCTIONS
def my_message(name):
    '''
    myMessage: this function prints a nice to meet you message to the user
    '''
    print('hello {}. It is nice to meet you'.format(name))
    return 0

def usage():
    print(__doc__)              #general docstring
    #print(my_message.__doc__)   #function docstring
    return 0


#MAIN
def main():
    print(len(sys.argv))
    try:
        my_message(sys.argv[1])
    except IndexError:
        usage()
        sys.exit()
    except:
        print("another error")
    return 0
    

if __name__ == '__main__':
    sys.exit(main())
