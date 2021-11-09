"""
Solution to the exercise from lecture05
Author: Ronald Wedema
Date: 01-09-2017
"""

class DNA:
    """
    Demo DNA class with basic sequence manipulation methods
    """

    def __init__(self, dna):
        """
        Method that will always run when object is created (instantiated)
        : param dna string with a dna sequence mandatory when creating the object
        """

        # check if the dna sequence is valid
        if self.is_valid_dna(dna):
            # only when valid store dna and get reverse complement
            self.sequence = dna
            self.rev_comp = self.get_reverse_complement()
        else:
            # best would be to raise your own errorclass here, topic of next lecture
            exit()

    def is_valid_dna(self, seq):
        """
        Method used for validity checking of a dna sequence

        : param seq string with a sequence to be tested
        : return is_dna a boolean
        """

        # define which bases are allowed
        valid_bases = 'ATCG'

        # set a boolean flag to represent if this is valid dna or not
        is_dna = True

        # loop over each base
        for base in seq:
            # check if this letter is not in the allowed bases
            if base not in valid_bases:
                # if letter not in allowed, then this is not valid dna
                return False

        # here return is used, no need to store this inside this object
        return is_dna

    def get_reverse_complement(self):
        """
        Method to get the reverse complement of a sequence

        : param seq string with dna sequence
        : return rev_comp_dna string with the reverse complemented dna sequence
        """

        # define variables
        complement_dna = ""
        complement_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}

        # loop over each base in the reversed dna sequence
        for base in self.sequence:
        # get the complement base from the dict and add to the complement_dna string
            complement_dna += complement_dict[base]

        # reverse the complement
        rev_comp_dna = complement_dna[::-1]

        return rev_comp_dna

    def dna_to_rna(self):
        """
        Method to create a rna sequence from dna

        : return string rna
        """

        rna = self.sequence.replace("T", "U")

        return rna

    def tranlate_dna_to_protein(self):
        """
        Method to tranlate a rna sequence to protein

        : return protein strin
        """

        # rna codons dictionary
        codon_table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'
        }

        # define empty string to hold the protein sequence
        protein = ''

        # make rna from dna
        rna = self.dna_to_rna()

        # determine max length, which is a multiplication of 3
        max_length_to_make_codons_off = len(rna) // 3 * 3

        # create indices to be used as slices for the codon creation
        for i in range(0, max_length_to_make_codons_off, 3):
            # slice from the rna block of 3 bases
            codon = rna[i: i + 3]
            # get the amino from the codon table
            protein += codon_table[codon]

        return protein

    def __repr__(self):
        """
        Method to be used when printing an object of type DNA

        : return string representation of this object
        """
        my_object_representation_as_string =  "DNA sequence: " + \
        self.sequence + "\nreverse complement: " + self.rev_comp

        return my_object_representation_as_string

def main():
    """
    One funtion to rule them all!
    """

    first_dna = DNA("ATGTAG")
    print(first_dna)
    print(first_dna.tranlate_dna_to_protein())

    second_dna = DNA("XXX")
    print(second_dna.rev_comp)
    print(second_dna)

if __name__ == '__main__':
    main()
