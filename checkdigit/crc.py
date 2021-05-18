# /usr/bin/env python
# This file is part of checkdigit.

# checkdigit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# checkdigit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with checkdigit.  If not, see <http://www.gnu.org/licenses/>.

"""Cyclic Redundancy Check.

A block of binary as a form of data validation is appended to a bitstring.
This can be easily checked even by very simple circuitry,
and can also be used to correct some errors.

WARNING: THIS IS NOT A FAST IMPLEMENTATION OF CRC.

If you want a fast implementation look elsewhere.


"""
from checkdigit._data import cleanse

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str, polynomial: str, pad: str = "0") -> str:
    """Adds a parity part onto the end of a block of data.

    Args:
        data: A string containing binary digits of any length
        polynomial: A string of binary digits representing the polynomial being used
        pad: "1" or "0" or nothing to be used to pad the data (defaults to 0)

    Returns:
        str: Check Value that should be appended to the stream

    Examples:
        >>> from checkdigit import crc
        >>> crc.calculate("1010", "1011")
        '011'
        >>> crc.calculate("100110010100111101111101", "11010111101")
        '0010001100'
    """
    data = cleanse(data)
    data += pad * (len(polynomial) - 1)
    bitarray = list(data)
    while len(bitarray) != len(polynomial) - 1:
        for (bit, _) in enumerate(polynomial):
            if polynomial[bit] == bitarray[bit]:
                bitarray[bit] = "0"  # XOR calculation
            else:
                bitarray[bit] = "1"
        while bitarray[0] == "0" and len(bitarray) >= len(polynomial):
            bitarray.pop(0)

    return "".join(bitarray)


def validate(data: str, polynomial: str) -> bool:
    """Validates whether the check digit matches a block of data.

    Args:
        data: A string containing binary digits including the check digit
        polynomial: Polynomial to use

    Returns:
        bool: A boolean representing whether the data is valid or not

    Examples:
        >>> from checkdigit import crc
        >>> crc.validate("1010101", "101")
        True
        >>> crc.validate("1000101", "101")
        False
    """
    data = cleanse(data)
    # the principle of CRCs is that when done again but with the check digit
    # appended if the data is fine it should all be 0s
    return "0" * (len(polynomial) - 1) == calculate(data, polynomial, "")


def missing(data: str, polynomial: str) -> str:
    """Calculates missing digits represented by a question mark.

    Args:
        data: A string containing a question mark representing a missing digit.
        polynomial: What the polynomial that should be used is

    Returns:
        str: The missing binary digit

    Examples:
        >>> from checkdigit import crc
        >>> crc.missing("?1111111101", "1101")
        '1'
        >>> crc.missing("10?110010100111?0?1111?10010?011?0", "11010111101")
        '011000'
        >>> # If there's more than one possible option
        >>> crc.missing("?1111111001", "1101")
        'Invalid'
    """
    solutions = []
    number = data.count("?")
    if number == 0:
        return "Invalid"  # if there are no ? to replace the algorithm will not work
    permutations = 2 ** number  # number of different permutations that are possible
    for permutation in range(permutations):
        tocheck = data
        replacement = bin(permutation)[2:].zfill(
            number
        )  # gives us a nice binary number
        for bit in replacement:
            tocheck = tocheck.replace("?", bit, 1)  # only replaces one bit at a time
        if validate(tocheck, polynomial):
            solutions.append(replacement)
            if len(solutions) == 2:
                return "Invalid"
    if len(solutions) == 1:
        return solutions[0]
    return "Invalid"
