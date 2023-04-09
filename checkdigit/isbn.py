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

"""International Standard Book Number.

ISBN codes are product identifiers used predominantly for books.
Support is provided for both ISBN-10 and ISBN-13.

"""

from checkdigit._data import cleanse, convert, missing_template


def calculate(data: str) -> str:
    """Calculates ISBN Check Digits.

    Args:
        data: A string of characters representing an ISBN code without the check digit

    Returns:
        str: The check digit that was missing

    Examples:
        >>> from checkdigit import isbn
        >>> # ISBN-10
        >>> isbn.calculate("043942089")
        'X'
        >>> # ISBN-13
        >>> isbn.calculate("978-1-86197-876")
        '9'
    """
    data = cleanse(data)

    if len(data) == 9:
        # ISBN 10 (without the check digit)
        # Multiply first digit by 10, second by 9, ... and take the sum
        total_sum = sum(
            int(digit) * weight for digit, weight in zip(data, range(10, 0, -1))
        )
        return convert(11 - (total_sum % 11))
    # elif not required since return above (and makes pylint happy)
    if len(data) == 12:
        # ISBN weights is 1 for odd positions and 3 for even
        # Since there are 12 digits, multiply weights by 6
        weights = (1, 3) * 6
        # Multiply each digit by its weight
        total_sum = sum(int(digit) * weight for digit, weight in zip(data, weights))
        # Return final check digit and type of barcode
        return convert(10 - (total_sum % 10), False)
    return "Invalid"


def validate(data: str) -> bool:
    """Validates ISBN check digits.

    Args:
        data: A string of characters representing a fall ISBN code

    Returns:
        bool: A boolean representing whether the
            check digit validates the data or non

    Examples:
        >>> from checkdigit import isbn
        >>> # ISBN-10
        >>> isbn.validate("0198526636")
        True
        >>> # ISBN-13
        >>> isbn.validate("978-1-56619-909-4")
        True
    """
    # The calculate method already cleanses the data.
    # If the return result is 'Invalid', it won't match the check digit (hence false).
    return calculate(data[:-1]) == data[-1]


def missing(data: str) -> str:
    """Calculates a missing digit in an ISBN Code represented by a question mark.

    Args:
        data: A string of characters representing a full ISBN code
            with a question mark representing a missing character

    Returns:
        str: The missing value that should've been where the question mark was

    Examples:
        >>> from checkdigit import isbn
        >>> # ISBN-10
        >>> isbn.missing("15688?111X")
        '1'
        >>> # ISBN-13
        >>> isbn.missing("978186197876?")
        '9'
        >>> isbn.missing("023456789128")
        'Invalid'
    """
    return missing_template(data, "isbn")
