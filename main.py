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
        "files/mems.txt", 
        "huffman"
    )
    
    program.run()
    
if __name__ == "__main__":
    main()