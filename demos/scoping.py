#!/usr/bin/env python3
"""
Explanation about Python scoping rules
"""

__author__ = "Jurre Hageman"

# any variable declared here is in the global name space. Its scope is global. The variable exists everywhere!

global_str = "I am a global variable, type = string" #global variable, type = str
global_int = 1 #global variable type = int
global_list = ["global list"] #global variable, type = list


def print_locals():
    # functions do have a local scope!
    # global variables can be accessed in the function scope!
    print("1. This works:", global_str)
    print("2. This works:", global_int)
    print("3. This works:", global_list)


#call print_locals
print_locals()


# define a new function
def manipulate_locals():
    #manipulating locals is not always allowed!

    # changing the string in place will NOT work! Remove hash of the next line to try
    # (note that strings are immutable so the change is always IN PLACE)
    #global_str += " I am changed" # >>> UnboundLocalError: local variable 'global_str' referenced before assignment

    # adding 1 to global_int will NOT work! Remove hash of the next line to try
    #global_int += 1 # >>> UnboundLocalError: local variable 'global_int' referenced before assignment

    # adding something to a global list is allowed BECAUSE LISTS ARE PASSED BY REFERENCE.
    # Therefore, altering an object inside a function/method will also change the original object outside the function in the global scope.
    global_list.append("I am new") #This works
    print("4.", global_list)


#call manipulate_locals
manipulate_locals()

# so now let's study this behaviour of the above:
list1 = ["hello"]
print("5. list1", list1) # >>> list1 ['hello']
list1.append(" world")
print("6. list1", list1) # >>> list1 ['hello', ' world']
list2 = list1
print("7. list2", list2) # >>> list2 ['hello', ' world']
list2.append("new element")
print("8. list2", list2) # >>> list2 ['hello', ' world', 'new element']
print("9. list1", list1) # >>> list1 ['hello', ' world', 'new element']
# So now both list 1 AND list 2 are changed because the variable names point to the SAME OBJECT in memory!
# THIS IS WHY YOU CAN CHANGE A GLOBAL LIST INSIDE A FUNCTION SCOPE
# To copy a list use slicing instead
list3 = list1[:] # slices from beginning to the very end
print("10. list3", list3) # >>> list3 ['hello', ' world', 'new element']
list3.append("yet another new element")
#List 3 is changed
print("11. list3", list3) # ['hello', ' world', 'new element', 'yet another new element']
#Note that list1 is not changed now
print("12. list1", list1) # list1 ['hello', ' world', 'new element']

# Scoping may seem annoying at first but it will be your friend in the future.
# You can now use the same variable name at multiple locations!

my_name = "Jaap"

def use_same_variable():
    my_name = "Piet"
    return my_name

print("13.", my_name) # >>> Jaap
# Now we call use_same_variable
print("14.", use_same_variable()) # >>> Piet

# Thus, we can use the same variable name inside different function declarations!

# So how do we change globals?
# We can use the keyword global inside the function.

def change_global():
    global global_int #use of the global keyword allows manipulation of the variable
    #this now works and does not throw the UnboundLocalError as seen before
    global_int += 1
    print("15.", global_int)

# call change_global
change_global()

# However, USING THE GLOBAL KEYWORD IS BAD PRACTICE!
# Make very limited use of global variables! Only something very general that is used very often and not subject to change is allowed to be in the global scope.

dna_bases = "atcg" #allowed global because it will not change and will be used often.

# for the rest: declare variables inside functions and pass them from function to function as arguments

def print_seq_upper(mssg): #mssg is a parameter that has been passed as an argument
    return mssg.upper() #returns mssg in upper case


def main():
    mssg = "I am a local variable"
    #call print_seq_upper and print results to screen
    print("16.", print_seq_upper(mssg)) #mssg is the argument passed to print_seq_upper

#call the main function
main()





