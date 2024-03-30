from program import Program

def main():
    """
    Run code.
    """

    program = Program("files/cano.txt", "huffman")
    program.run()
    
if __name__ == "__main__":
    main()