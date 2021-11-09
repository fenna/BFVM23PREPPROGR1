"""
Solution to the exercise from lecture04
Author: Ronald Wedema
Date: 01-09-2017
"""

# import the sys module to get the commandline arguments
import sys

def get_files_from_commandline():
    """
    Function to get commandline arguments

    : return tuple with 2 files, first is the in file, second is the out file
    """

    # use the correct indices to get the commandline arguments
    # (0 index is the module name, skip this one!)
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    return in_file, out_file


def read_content(in_file):
    """
    Function to get the content of a (multi) fasta file

    : param string with in file name
    : return a dictionary with key = header and value = sequence
    """

    # define variables
    sequence_dict = {}
    header = ''

    # neat method to open a file and have it close automatically (with())
    with open(in_file) as file_reader:
        # read line
        for line in file_reader:
            # remove newline
            line = line.strip()

            # check if this line starts with a > symbol, meaning we have a header
            if line.startswith(">"):
                header = line
                # store this header in the dictionary and assign it a empty string as value
                sequence_dict[header] = ''
            # not a header, than it most be a sequence
            else:
                # add this line to the previously seen header in the dict
                sequence_dict[header] += line

    return sequence_dict


def get_reverse_complement(seq):
    """
    Function to get the reverse complement of a sequence

    : param seq string with dna sequence
    """

    # define variables
    complement_dna = ""
    complement_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}

    # loop over each base in the reversed dna sequence
    for base in seq:
    # get the complement base from the dict and add to the complement_dna string
        complement_dna += complement_dict[base]

    # reverse the complement
    rev_comp_dna = complement_dna[::-1]

    return rev_comp_dna


def write_file(file_writer, content):
    """
    Function to write content to a file

    : param file_writer a file handler object
    : content string with the content to be written
    """

    # write the content
    file_writer.write(content)


def main():
    """
    One function to rule them all!
    """

    # get commandline arguments
    in_file, out_file = get_files_from_commandline()
    # read the infile
    fasta_dict = read_content(in_file)

    # open a file to write to
    with open(out_file, mode='w') as fasta_writer:
        # get key and values from the dict
        for header, sequence in fasta_dict.items():
            # reverse and complement the sequence
            rev_comp = get_reverse_complement(sequence)

            # write the header and sequence to a file
            write_file(fasta_writer, header + "\n")
            write_file(fasta_writer, rev_comp + "\n")

# check if this is the main running module
if __name__ == '__main__':
    main()
