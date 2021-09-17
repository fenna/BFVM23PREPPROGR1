#!/usr/bin/env python3

"""
Docstring explaining these are the solutions to the assessment exam
"""

__author__ = 'Ronald Wedema'
__version__ = '1.0'

from sub_module import my_own_function


def question1():
    """"
    Can use different data types (3 questions total 9 points)

    # Q1 (3 points):
    Create a string variable called q1_1 that will hold the following text: I will rock this exam!

    # Q2 (3 points):
    Create a dictionary variable called q1_2 that will hold the combination of first name and last name of students.
    For this you can use mock students.

    # Q3 (3 points):
    Given the next problem what datatype would you use. Explain in clear wording why you choose this datatype.
    Problem: Program needs to store many different measured student heights in cm. Save your answer in a variable called
    q3_3
    :return:
    """

    print("q1")
    q1_1 = "I will rock this exam!"
    q1_2 = {"Pietje": "Puck", "TestStudent": "TestStudentLastName"}
    q1_3 = "List"

    print(q1_1, q1_2, q1_3)


def question2():
    """
    Can use Python flow and control logic (3 questions 15 points)
    Use the following numbers for each question: 1,2,3,4,5,6

    # Q1 (10 points): use a for loop combined with an if/else loop that will:
    # print the number and even for even numbers and odd for odd numbers

    # Q2 (5 points): use a while loop
    # iterate the numbers using a while loop

    :return:
    """
    my_list = [1, 2, 3, 4, 5, 6]

    print("q2_1")
    for i in my_list:
        if i % 2 == 0 in my_list:
            print(str(i) + " even")
        else:
            print(str(i) + " odd")

    print("q2_2")
    i = 1
    while i < len(my_list) + 1:
        print(i)
        i += 1


def question3():
    """
    Can implement functions, make use of modules , write text files (3 questions 21 points)

    # Q1: Implement function (7 points)
    # Create a separate function for every question in this test

    # Q2: create a function to_be_imported inside a module called sub_module and import it in this script (7 points)
    # the function should determine the length of a word given as an argument and return it
    # Catch the length of the word and print it here

    # Q3: create a function that will read a filename given as argument and write this text file (modified) using
    # with(open). Every line from the file should be read using with(open), remove line enters (newlines).
    # Skip the header line (starting with > and write the non header lines to a new file called q3_output.txt (7 points)

    :return:
    """

    print("q3_2")
    counted = my_own_function("Count this.....")
    print(counted)

    def q3_3(file_in):

        outline = ""
        with(open("q3_output.txt", "w")) as fw:
            with(open(file_in)) as fh:
                for line in fh:
                    line = line.strip()
                    if not line.startswith(">"):
                        outline += line
            fw.write(outline + "\n")

    print("q3_3")
    q3_3("test_in.fa")


def question4():
    """
    Can implements exceptions handling (1 question 5 points)
    Create own exception class Not42 inheriting from the base Exception class.
    Iterare the following numbers: 1, 2, 3, 42, 5, 6
    Throw the exception Not42 on NOT finding the number 42
    Catch this error and print: 42 not found when this error is catched or: Answer to everything found otherwise

    :return:
    """

    class Not42(Exception):
        pass

    for number in [1, 2, 3, 42, 5, 6]:
        try:
            if number != 42:
                raise Not42
            else:
                print("Answer to everything found!")
        except Not42:
            print("42 not found")


def question5():
    """
    Can write, document, test and implement software products (3 questions 20 points)

    # Q1: rewrite this script so that all functions are called from a central main function
    add a correct sha-bang to this script you may use the following location for the sha-bang line: /usr/bin/env python3
    add a check to test of this is the main running script, and only when this is the main script call the main function
    (5 points)

    # Q2: Add Python documentation in the correct format on the module level and also for every function you've created
    add some inline comments to show that you know how to write these (5 points)

    # Q3: Debug the following piece of code (10 points)
    def fixed:
        import: sys
        print sys.vesion
        x = 'this correct??"
        y
        for i in x;
            y =+ i

        if length(y) * 3 = 42
            outcome == "Great succes!"
        else
            outcome == "bummer"

        return outcome

    print(fixed)


    :return:
    """
    # Q1
    # first line should be: #!/usr/bin/env python3
    # next should be the import
    # the functions should follow the imports
    # the main function should call all other functions
    # if __name__ == "__main__" check to test if this is the running script

    # Q2
    # Triple double qoutes for module descrition and every function with description, arguments and return
    # #comment lines describing some piece of code

    print("q5_3")

    def fixed():
        import sys
        print(sys.version)
        x = 'this correct??'
        y = ''
        for i in x:
            y += i

        if len(y) * 3 == 42:
            outcome = "Great succes!"
        else:
            outcome = "bummer"

        return outcome

    print(fixed())


def question6():
    """
    Can translate a given problem into a robust and flexible object-oriented software design (3 questions 20 points)

    # Q1: (5 points)
    Create a class Course that can be used to store the following information:
    - Course name
    - Course lecturer
    - Course exam form, can be one of: Assignment or exam
    - holds a list with student names attending the course

    # Q2 (5 points)
    When the class is created, it should be created with the Course name and lecturer it should also keep track of
    the number of created classes, save this in a class variable called number_of_courses

    # Q3 (5 points)
    It should have the following methods:
        get number of students in class
        add student(s) names to a list, as long as there is less than 15 students in the class,
            If there are more than 15 print: class is full!
        set the exam form, check if it is one of assignment or exam and than assign this to the class
            If the exam_form is not allowed, show this by printing form not allowed

    Finally, show that your class can be used by creating three courses: python, datascience and omics, If you dont know
    who teaches, just use a fake name here.
    Print the number of total Course classes created by printing the class variable of one the course.
    try to set the exam form of omics to practical
    Add a bunch (minimal 2) students to a course
    and lastly print the number of students in that course

    :return:
    """

    class Course:

        number_of_course = 0

        def __init__(self, course_name, lecturer):
            Course.number_of_course += 1
            self.course_name = course_name
            self.lecturer = lecturer
            self.student_list = []
            self.exam_form = ""

        def get_student_count(self):
            return len(self.student_list)

        def set_exam_form(self, exam_form):
            if exam_form in ("Assignment", "Exam"):
                self.exam_form = exam_form
            else:
                print("not an allowed exam form")

        def add_students(self, *student_name):
            for student in student_name:
                if self.get_student_count() < 15:
                    self.student_list.append(student)
                else:
                    print("class is full!")

    python = Course("Python", "WERD")
    datascience = Course("DataScience", "LADR")
    omics = Course("Omics", "HJUR")

    print(omics.number_of_course)

    datascience.set_exam_form("practical")

    python.add_students("ronald", "fenna")
    print(python.get_student_count())


def question7():
    """
    Advanced Python concepts: *args, **kwargs, decorators, generators, comprehensions (2 questions 10 points)

    Q1: Create a function that will use the Python **kwargs concept.
    Show that your function works by calling it twice with different arguments
    (5 points)

    Q2: Use list comprehension to calculate the inverse of a number (1/number)
    and than calculates that number to the third power
    do this for each number in the following list: 1, 2, 3, 4, 5, 6.
    store the results in a tuple, use round to round the inverse before you save it in the tuple (5 points)

    Expected result:
   [(1, 1), (0, 8), (0, 27), (0, 64), (0, 125), (0, 216)]

    :return:
    """

    def q7_1(**kwargs):
        for k, v in kwargs.items():
            print(k, v)

    print("q7_1")
    q7_1(x=2, y=4)
    q7_1(x=2, y=4, z="bla")

    list_of_tuples = [(round(1/x), x**3) for x in [1, 2, 3, 4, 5, 6]]
    print(list_of_tuples)


def main():
    """
    Every function should be called from the main

    :return:
    """

    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()


if __name__ == "__main__":
    main()
