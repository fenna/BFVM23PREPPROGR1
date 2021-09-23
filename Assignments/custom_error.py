#!/usr/bin/env python3

"""
Solution to week6 exercises
author: Ronald Wedema
Version:1
Date: October - 2020
"""


class NotDnaBaseError(Exception):
    pass


def validate(seq):
    """
    function to check if a sequence is valid dna
    Raise an error if a base is found that is not A, C, T, or G
    :param seq:
    :return:
    """

    allowed_bases = ("A", "C", "T", "G")

    valid_dna = True

    for base in seq:
        if base not in allowed_bases:
            valid_dna = False

    if not valid_dna:
        raise NotDnaBaseError
    else:
        return seq
