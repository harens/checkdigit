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

"""GS1 Validation Functions."""

import math

from checkdigit._data import cleanse, convert

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str) -> str:
    """Calculates GS1 Check Digit.

    This method works for all fixed length numeric GS1 data structures
    (including GDTI, GLN, GRAI, etc.) that require a check digit.

    Args:
        data: A string of characters

    Returns:
        str: The check digit that was missing
    """
    data = cleanse(data)
    data = data[::-1]  # Reverse the barcode, as last digit is always multiplied by 3
    total_sum = 0
    for index, value in enumerate(data):
        if index % 2 == 0:
            total_sum += int(value) * 3
        else:
            total_sum += int(value)
    next_multiple_of_ten = int(math.ceil(total_sum / 10.0)) * 10
    check_digit = next_multiple_of_ten - total_sum
    return convert(check_digit, "gs1")


def validate(data: str) -> bool:
    """Validates GS1.

    This method works for all fixed length numeric GS1 data structures
    (including GDTI, GLN, GRAI, etc.) that require a check digit.

    Args:
        data: A string of characters representing a full GS1 code

    Returns:
        bool: A boolean representing whether the
            check digit validates the data or not

    """
    data = cleanse(data)
    return calculate(data[:-1]) == data[-1]


def missing(data: str) -> str:
    """Calculates a missing digit in a GS1 Code.

    This method works for all fixed length numeric GS1 data structures
    (including GDTI, GLN, GRAI, etc.) that require a check digit.

    Args:
        data: A string of characters representing a full ISBN code
            with a question mark representing a missing character

    Returns:
        str: The missing value that should've been where the question mark was

    Examples:
        >>> from checkdigit import gs1
        >>> gs1.missing("?8945528")
        '9'
        >>> gs1.missing("992802?035392")
        '2'
        >>> gs1.missing("084085752492131?31")
        '7'
        >>> gs1.missing("846684302750007275")
        'Invalid'

    """
    data = cleanse(data)
    for poss_digit in range(10):  # Brute Force the 10 options
        option = convert(poss_digit)
        # tests it with the generated number
        # If this fails, the next number is tried
        if validate(data.replace("?", option)):
            return option
    return "Invalid"
