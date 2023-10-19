#!/usr/bin/env python3
"""
   demonstrate simple generator
"""

# Metadata variables
__author__ = "Fenna Feenstra"
__status__ = "0.1"

import math
import sys

def simple_generator():
    yield 11
    yield 22
    yield 33

def infinitive_generator():
    gen = 11
    while True:
        yield gen
        gen += 11

def call_three_times():
    my_gen = simple_generator()
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    return

def call_with_args():
    my_gen = simple_generator()
    print(*my_gen)
    return

def call_with_loop():
    for gen in simple_generator():
        print(gen)
    return

def call_with_error():
    my_gen = simple_generator()
    try:
        print(next(my_gen))
        print(next(my_gen))
        print(next(my_gen))
        print(next(my_gen))
    except StopIteration:
        print("oops, out of range")
    finally:
         return
     
def call_infinitive_gen(max):
    for gen in infinitive_generator():
        if gen < max:
            print(gen)
        else: return



def main():
    call_three_times()
    call_with_args()
    call_with_loop()
    call_with_error()
    call_infinitive_gen(34)
    return


if __name__ == "__main__":
    sys.exit(main())

