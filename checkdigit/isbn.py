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

"""ISBN Validation Functions.

ISBN codes are product identifiers used predominantly for books.

Note that the ISBN-13 functions can also be used for EAN-13 and Bookland codes.

"""

from checkdigit._data import cleanse, convert

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate10(data: str) -> str:
    """Calculates ISBN-10 Check Digit.

    Args:
        data: A string of 9 characters

    Returns:
        str: The check digit that was missing

    Examples:
        >>> from checkdigit import isbn
        >>> isbn.calculate10("006196436")
        '0'
        >>> isbn.calculate10("043942089")
        'X'
    """
    data = cleanse(data)
    # Multiply first digit by 10, second by 9, ... and take the sum
    total_sum = sum(
        int(digit) * weight for digit, weight in zip(data, range(10, 0, -1))
    )
    return convert(11 - (total_sum % 11))


def validate10(data: str) -> bool:
    """Validates ISBN-10.

    Args:
        data: A string of characters representing a full ISBN-10 code

    Returns:
        bool: A boolean representing whether the
            check digit validates the data or not

    Examples:
        >>> from checkdigit import isbn
        >>> isbn.validate10("1-56619-909-3")
        True
        >>> isbn.validate10("0198526636")
        True
        >>> isbn.validate10("423423")
        False
    """
    data = cleanse(data)
    return calculate10(data[:-1]) == data[-1]


def calculate13(data: str, barcode: str = "isbn") -> str:
    """Calculates ISBN-13 Check Digit.

    Args:
        data: A string of 12 characters
        barcode: The type of code (either isbn or upc)

    Returns:
        str: The check digit that was missing

    Examples:
        >>> from checkdigit import isbn
        >>> isbn.calculate13("978-1-86197-876")
        '9'
        >>> isbn.calculate13("012345678912")
        '8'
    """
    data = cleanse(data)
    # ISBN weights is 1 for odd positions and 3 for even
    # The opposite is true for upc
    weights = (1, 3) * 6 if barcode == "isbn" else (3, 1) * 6
    # Multiply each digit by its weight
    total_sum = sum(int(digit) * weight for digit, weight in zip(data, weights))
    # Return final check digit and type of barcode
    return convert(10 - (total_sum % 10), barcode)


def validate13(data: str) -> bool:
    """Validates ISBN-13.

    Args:
        data: A string of characters representing a full ISBN-13 code

    Returns:
        bool: A boolean representing whether the check digit validates the data

    Examples:
        >>> from checkdigit import isbn
        >>> isbn.validate13("978-1-56619-909-4")
        True
        >>> isbn.validate13("0123456789128")
        True
        >>> isbn.validate13("1234")
        False

    """
    data = cleanse(data)
    return calculate13(data[:-1]) == data[-1]


def missing(data: str) -> str:
    """Calculates a missing digit in an ISBN Code represented by a question mark.

    Args:
        data: A string of characters representing a full ISBN code
            with a question mark representing a missing character

    Returns:
        str: The missing value that should've been where the question mark was

    Examples:
        >>> from checkdigit import isbn
        >>> isbn.missing("15688?111X")
        '1'
        >>> isbn.missing("978186197876?")
        '9'
        >>> isbn.missing("023456789128")
        'Invalid'
    """
    data = cleanse(data)
    data_length = len(data)  # ISBN-10 or 13
    # We already have an efficient method for the checkdigit
    if data[-1] == "?":
        # Remove question mark check digit
        return calculate10(data[:-1]) if data_length == 10 else calculate13(data[:-1])

    # We've dealt with the check digit, so X can't be an option
    # Brute force all the possible numbers (0-9 inclusive)
    for option in (data.replace("?", str(i)) for i in range(10)):
        # Validate the new option
        if (
            data_length == 10
            and validate10(option)
            or data_length == 13
            and validate13(option)
        ):
            # Replace question mark with new value
            return option[data.index("?")]
    return "Invalid"
