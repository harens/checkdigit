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

For more information, please look at the wiki page for this module:
https://add.wiki.page.here

"""

from checkdigit._data import cleanse

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str, polynomial: str, pad: str = "0") -> str:
    """Adds a parity bit onto the end of a block of data.

    Args:
        data: A string containing binary digits of any length
        polynomial: A string of binary digits representing the polynomial being used
        pad: "1" or "0" or nothing to be used to pad the data (defaults to 0)

    Returns:
        str: Check Value that should be appended to the stream
    """
    data = cleanse(data)
    data += pad * (len(polynomial) - 1)
    bitarray = list(data)
    while len(bitarray) != len(polynomial) - 1:
        for bit in range(len(polynomial)):
            if polynomial[bit] == bitarray[bit]:
                bitarray[bit] = "0"  # XOR calculation
            else:
                bitarray[bit] = "1"
        while bitarray[0] == "0" and len(bitarray) >= len(polynomial):
            bitarray.pop(0)

    return cleanse("".join(bitarray))


def validate(data: str, polynomial: str) -> bool:
    """Validates whether the check digit matches a block of data.

    Args:
        data: A string containing binary digits including the check digit
        polynomial: Polynomial to use

    Returns:
        bool: A boolean representing whether the data is valid or not
    """
    data = cleanse(data)
    # the principle of CRCs is that when done again but with the check digit
    # appended if the data is fine it should all be 0s
    return "0" * (len(polynomial) - 1) == calculate(data, polynomial, "")
