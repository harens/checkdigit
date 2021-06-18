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

"""Global Trade Identification Numbers.

This includes support for the following:

- Bookland
- EAN-13
- EAN-8
- ISBN-10
- ISBN-13
- UPC-A

"""

from checkdigit._data import cleanse, convert

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str, isbn: bool = False) -> str:
    """Calculates GTIN-based Check Digits.

    Args:
        data: A string of characters representing the code
        isbn: Whether the code is ISBN-based or not. Else, it assumes it's EAN/UPC

    Returns:
        str: The check digit that was missing

    Examples:
        >>> from checkdigit import gtin
        >>> # ISBN-10
        >>> gtin.calculate("043942089", True)
        'X'
        >>> # ISBN-13
        >>> gtin.calculate("978-1-86197-876", True)
        '9'
        >>> # UPC-A
        >>> gtin.calculate("17593487596")
        '0'
        >>> # EAN-8
        >>> gtin.calculate("5512345")
        '7'
    """
    data = cleanse(data)

    if len(data) == 9 and isbn:
        # ISBN 10 (without the check digit)
        # Multiply first digit by 10, second by 9, ... and take the sum
        total_sum = sum(
            int(digit) * weight for digit, weight in zip(data, range(10, 0, -1))
        )
        return convert(11 - (total_sum % 11))
    # elif not required since return above (and makes pylint happy)
    if (len(data) == 12 and isbn) or not isbn:
        # ISBN weights is 1 for odd positions and 3 for even
        # The opposite is true for EAN/UPC
        weights = (1, 3) * 6 if isbn else (3, 1) * 6
        # Multiply each digit by its weight
        total_sum = sum(int(digit) * weight for digit, weight in zip(data, weights))
        # Return final check digit and type of barcode
        return convert(10 - (total_sum % 10), isbn)
    return "Invalid"


def validate(data: str, isbn: bool = False) -> bool:
    """Validates GTIN-based check digits.

    Args:
        data: A string of characters representing a fall GTIN code
        isbn: Whether the code is ISBN-based or not. Else, it assumes it's EAN/UPC

    Returns:
        bool: A boolean representing whether the
            check digit validates the data or non

    Examples:
        >>> from checkdigit import gtin
        >>> # ISBN-10
        >>> gtin.validate("0198526636", True)
        True
        >>> # ISBN-13
        >>> gtin.validate("978-1-56619-909-4", True)
        True
        >>> # UPC-A
        >>> gtin.validate("672792398018")
        True
        >>> gtin.validate("672792398017")
        False
    """
    # The calculate method already cleanses the data.
    # If the return result is 'Invalid', it won't match the check digit (hence false).
    return calculate(data[:-1], isbn) == data[-1]


def missing(data: str, isbn: bool = False) -> str:
    """Calculates a missing digit in a GTIN Code represented by a question mark.

    Args:
        data: A string of characters representing a full ISBN code
            with a question mark representing a missing character
        isbn: Whether the code is ISBN-based or not. Else, it assumes it's EAN/UPC

    Returns:
        str: The missing value that should've been where the question mark was

    Examples:
        >>> from checkdigit import gtin
        >>> # ISBN-10
        >>> gtin.missing("15688?111X", True)
        '1'
        >>> # ISBN-13
        >>> gtin.missing("978186197876?", True)
        '9'
        >>> # UPC-A
        >>> gtin.missing("61?141000036")
        '4'
        >>> gtin.missing("023456789128")
        'Invalid'
    """
    # We already have an efficient method for the check digit
    if data[-1] == "?":
        # Remove question mark check digit
        return calculate(data[:-1], isbn)

    # We've dealt with the check digit, so X can't be an option
    # Brute force all the possible numbers (0-9 inclusive)
    for option in (data.replace("?", str(i)) for i in range(10)):
        # Validate the new option
        if validate(option, isbn):
            # Replace question mark with new value
            return option[data.index("?")]
    return "Invalid"
