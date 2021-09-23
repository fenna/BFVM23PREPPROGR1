#!/usr/bin/env python3

"""
Solution to week5 exercises
author: Ronald Wedema
Version:1
Date: October - 2020
"""


class Student:
    """
    Base class student
    """

    # class variables
    list_of_all_student_names = []
    total_students_created = 0

    def __init__(self, first_name, last_name, my_class):
        """
        Every Student has to be created with:
        :param first_name: string with a first name
        :param last_name: string with the surname
        :param my_class: string holding class of the studente
        """

        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.my_class = my_class
        self.tutor = ''
        self.age = None

        Student.list_of_all_student_names.append(first_name)
        Student.total_students_created += 1

    def say_name(self):
        """
        Method to print the first and last name of a student
        :return: None
        """

        print("Hello my name is {} {}".format(self.first_name, self.last_name))

    def __str__(self):
        """
        String override method
        :return: string representation of the object state
        """
        return "first name: {}\nlast name: {}\nclass: {}".format(self.first_name, self.last_name, self.my_class)

    def set_age(self, age):
        """
        Set the age of the object if age > 16
        :param age: int age
        :return:
        """

        if age > 16:
            self.age = age
        else:
            print("Age is not sufficient")


class MasterStudent(Student):
    """
    Master student class inheriting from base Student
    """

    def __init__(self, previous_education, first_name, last_name, my_class):
        """
        Add previous eduction on top of the init of Student
        :param previous_education:
        :param first_name:
        :param last_name:
        :param my_class:
        """
        self.prev_edu = previous_education
        # we have to call the "super" class of Masterstudent (Student), to also fulfill it's __init__ method
        super(MasterStudent, self).__init__(first_name, last_name, my_class)


def main():
    ronald = Student("ronald", "Wedema", "PrepProgramming")
    isabeau = Student("Isabeau", "Wedema", "PrimarySchool")
    olivier = Student("Olivier", "Wedema", "PrimarySchool")
    pietje = Student("Pietje", "Puk", "DataScience")
    kees = Student("Kees", "lastName", "Stats")

    ronald.say_name()
    isabeau.say_name()
    olivier.say_name()
    pietje.say_name()
    kees.say_name()

    print(ronald)

    isabeau.set_age(12)
    olivier.set_age(18)

    print(kees.list_of_all_student_names)
    print(kees.total_students_created)

    master_student = MasterStudent("Bio-Informatics", "FirstName", "LastName", "PrepProgramming")
    print(master_student)


if __name__ == "__main__":
    main()
