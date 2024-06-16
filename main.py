#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python program to encode text files into videos
"""

from scripts.program import Program
from scripts.comparator import Comparator

def main():
    """
    Run code.
    """

    program0 = Program( 
        file_path="files/txt/test.txt", 
        coding_method="huffman",
        args=[["0", "1"]]
    )

    program0.run()

    program1 = Program(
        file_path="files/txt/test.txt", 
        coding_method="block",
        args=[["0", "1"]]
    )

    program1.run()
    
    comparator = Comparator([program0, program1])
    comparator.compare()

if __name__ == "__main__":
    main()

"""
program = Program(
    file_path="files/test.txt", 
    coding_method="block",
    args=[["0", "1"]]
)
"""