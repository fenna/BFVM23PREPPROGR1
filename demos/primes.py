
#!/usr/bin/env python3
"""
generate sexy primes
"""

# Metadata variables
__author__ = "Fenna Feenstra"
__status__ = "first try"

import math
import sys


def is_prime(number):
    ''' check if this is a prime number'''
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


def get_primes(number):
    '''prime number generator from a number till infinity...'''
    while True:
        if is_prime(number):
            yield number
        number += 1

        
def get_sexy_prime_doubles(startval, endval):
    '''check the sexy prime condition till the max and count them'''
    count_prime_doubles = 0
    #start to generate prime numbers with for loop and get_primes generator
    for next_prime in get_primes(startval):
        if next_prime < endval:
            if is_prime(next_prime+6):
                print("({}, {})".format(next_prime, next_prime+6))
                count_prime_doubles += 1
        else:
            return count_prime_doubles


def main():
   print('total sexy primes doubles: {}'.format(get_sexy_prime_doubles(0,200)))

if __name__ == "__main__":
    sys.exit(main()) 
