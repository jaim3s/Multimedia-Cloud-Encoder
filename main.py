from program import Program

def main():
    """
    Run code.
    """

    program = Program("files/mems.txt", "huffman")
    program.run()
    
if __name__ == "__main__":
    main()