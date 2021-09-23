#!/usr/bin/env python3

"""
Solution to week3 exercises
author: Ronald Wedema
Version:1
Date: October - 2020
"""

import math


def calculate_area_square(length):
    """
    Function to calculate area of a square given a length
    :param length: int
    :return: total area calculated
    """

    total_area = length ^ 2
    return total_area


def calculate_area_rectangle(width, height):
    """
    Function to calculate the area of a rectangle
    :param width: int width of the rectangle
    :param height: int height of the rectangle
    :return: total area calculated
    """

    total_area = width * height
    return total_area


def calculate_area_circle(radius):
    """
    Function to calculate the area of a circle
    :param radius: radius of circle
    :return: total area calculated
    """

    total_area = math.pi * float(radius ^ 2)
    return round(total_area)


def calculate_area_triangle(width, height):
    """
    Function to calculate the area of a triangle
    :param width: width of triangle
    :param height: height of triangle
    :return: total area calculated
    """

    square_area = calculate_area_rectangle(width, height)
    total_area = square_area / 2

    return total_area


def main():
    total_square = 25
    if calculate_area_square(5) == total_square:
        print("square area calculated correctly")

    total_rectangle = 30
    if calculate_area_rectangle(3, 10) == total_rectangle:
        print("rectangle area calculated correctly")

    total_triangle = 15
    if calculate_area_triangle(3, 10) == total_triangle:
        print("triangle area calculated correctly")

    total_circle = 22
    if calculate_area_circle(5) == total_circle:
        print("circle area calculated correctly")


if __name__ == "__main__":
    main()
