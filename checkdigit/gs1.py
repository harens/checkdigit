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

"""Global Standards One.

GS1 provides a variety of different standards

This implementation includes support for the following:

- GSIN
- GLN
- GRAI
- GTIN-8/12/13/14
    - EAN-8
    - EAN-13
    - UPC-A
    - UPC-E
- SSCC
- etc. (all fixed length numeric GS1 data structures with a check digit)
"""

import math

from checkdigit._data import cleanse, convert, missing_template


def calculate(data: str) -> str:
    """Calculates GS1 Check Digit.

    This method works for all fixed length numeric GS1 data structures
    (including GDTI, GLN, GRAI, etc.) that require a check digit.

    Args:
        data: A string of characters

    Returns:
        str: The check digit that was missing

    Examples:
        >>> from checkdigit import gs1
        >>> gs1.calculate("00199999980000110")
        '7'
        >>> gs1.calculate("67368623738347505")
        '1'
    """
    data = cleanse(data)
    data = data[::-1]  # Reverse the barcode, as last digit is always multiplied by 3
    # Follows order 3, 1, 3, etc.
    # Use ceil to ensure all digits of data are matched with a weight (round up division)
    weights = (3, 1) * math.ceil(len(data) / 2)
    # Multiply each digit by its weight
    total_sum = sum(int(digit) * weight for digit, weight in zip(data, weights))
    # Return final check digit and type of barcode
    return convert(10 - (total_sum % 10), False)


def validate(data: str) -> bool:
    """Validates GS1.

    This method works for all fixed length numeric GS1 data structures
    (including GDTI, GLN, GRAI, etc.) that require a check digit.

    Args:
        data: A string of characters representing a full GS1 code

    Returns:
        bool: A boolean representing whether the
            check digit validates the data or not

    Examples:
        >>> from checkdigit import gs1
        >>> gs1.validate("224245438987081447")
        False
        >>> gs1.validate("961552634342856982")
        True
    """
    # Data is cleansed by the calculate function
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
    return missing_template(data, "gs1")
