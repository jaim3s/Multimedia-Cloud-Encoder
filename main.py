#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python program to encode text files into videos
"""

from scripts.program import Program

def main():
    """
    Run code.
    """

    program = Program(
        file_path="files/test.txt", 
        coding_method="huffman",
        args=[["0", "1"]]
    )
    
    program.run()
    
if __name__ == "__main__":
    main()

"""
program = Program(
    file_path="files/test.txt", 
    coding_method="block",
    args=[["0", "1"]]
)
"""