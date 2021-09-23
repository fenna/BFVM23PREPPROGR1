#!/usr/bin/env python3

"""
Solution to week4 exercises
author: Ronald Wedema
Version:1
Date: October - 2020
"""

import sys


def read_fasta(file_in):
    """
    Function to read a fasta formatted file
    :param file_in: fasta file name to be read
    :return: dictionary containing headers as key and sequence as value
    """

    fasta_dict = {}
    header = ''

    # us with open to read a file, file will be closed automagically
    with open(file_in, mode="r") as file_in_handler:
        for line in file_in_handler:
            line = line.strip()  # remove newline (enters)
            if line.startswith(">"):  # do we have a header sequence
                header = line.replace(">", "")
                fasta_dict[header] = ""
            else:
                fasta_dict[header] = line
                header = ''

    return fasta_dict


def reverse_complement(seq):
    """
    Function to determine the reverse complement of a sequence
    :param seq: string of nucleotides
    :return: reverse complement of the string
    """

    comp_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

    comp_seq = ''

    # iterate the sequence and get complement
    for base in seq:
        comp_seq += comp_dict[base]

    # reverse the sequence
    comp_rev_seq = comp_seq[::-1]

    return comp_rev_seq


def main():
    fasta_file = sys.argv[1]
    my_fasta_dict = read_fasta(fasta_file)

    # iterate and write every header + sequence
    with open("out_fasta.fasta", mode="w") as out_file_handler:
        for header, sequence in my_fasta_dict.items():
            rev_comp_seq = reverse_complement(sequence)
            out_file_handler.write(">" + header + "\n" + rev_comp_seq + "\n")


if __name__ == "__main__":
    main()
