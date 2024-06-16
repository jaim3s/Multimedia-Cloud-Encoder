def zero_pad_right(binary_string: str,  length: int) -> str:
    """
    Add zeros to fit the length.

        Parameters
            binary_string (str): Binary string to fit the size
            length (int): Length to fit the binary string

        Returns
            return Binary string filled with zeros to the left
    """

    return binary_string + "0" * (length - len(binary_string))

def character_to_binary(ch: str, length: int) -> str:
    """
    Convert the string character into a binary string.

        Parameters
            ch (str): Character to convert in binary
            length (int): Length to fit the binary string

        Returns
            return Binary representation of the character
    """

    return bin(ord(ch))[2:].zfill(length)

def binary_to_character(bin_ASCII: str) -> str:
    """
    Convert the binary ASCII string in a character.

        Parameters
            bin_ASCII (str): Binary ASCII string to convert

        Returns
            return Character of the binary ASCII string
    """

    return chr(int(bin_ASCII, 2))


def int_to_bin_right_padding(num: int, n: int) -> str:
    """
    Convert integer to binary with n number of bits.

        Parameters
            num (int): Integer to convert
            n (int): Number of bits

        Returns
            return A string representing the binary number of the integer
    """

    return zero_pad_right(str(bin(num)[2:]), n)

def int_to_bin_left_padding(num: int, n: int) -> str:
    """
    Convert integer to binary with n number of bits.

        Parameters
            num (int): Integer to convert
            n (int): Number of bits

        Returns
            return A string representing the binary number of the integer
    """

    return str(bin(num)[2:]).zfill(n)

