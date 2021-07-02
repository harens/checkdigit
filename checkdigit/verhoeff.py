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

"""The first check digit algorithm to detect all transposition and single digit errors.

Developed by Jacobus Verhoeff and published in 1969.
This particular implementation uses a table-based algorithm.
"""

from checkdigit._data import TupleType, cleanse, missing_template

DIHEDRAL_CAYLEY: TupleType[TupleType[int]] = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
    (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
    (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
    (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
    (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
    (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
    (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
    (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
)

INVERSE: TupleType[int] = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

PERMUTATION: TupleType[TupleType[int]] = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
    (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
    (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
    (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
    (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
    (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
    (7, 0, 4, 6, 9, 1, 3, 2, 5, 8),
)


def calculate(data: str) -> str:
    """Calculates a Verhoeff check digit.

    Args:
        data: A block of data without the check digit

    Returns:
        str: A string representing the missing check digit

    Examples:
        >>> from checkdigit import verhoeff
        >>> verhoeff.calculate('236')
        '3'
        >>> verhoeff.calculate('123456')
        '8'
        >>> verhoeff.calculate('1337')
        '5'
    """
    checksum = 0
    data = cleanse(data)
    # Start counting from 1 (hence enumerate(..., 1))
    for count, value in enumerate(data[::-1], 1):
        checksum = DIHEDRAL_CAYLEY[checksum][PERMUTATION[count % 8][int(value)]]
    return str(INVERSE[checksum])


def validate(data: str) -> bool:
    """Validates a Verhoeff check digit.

    Args:
        data: A string of characters representing a full Verhoeff code.

    Returns:
        bool: A boolean representing whether the check digit validates the data or not.

    Examples:
        >>> from checkdigit import verhoeff
        >>> verhoeff.validate('585649')
        True
        >>> verhoeff.validate('13735')
        False
    """
    return calculate(data[:-1]) == data[-1]


def missing(data: str) -> str:
    """Calculates a missing digit in a Verhoeff code.

    Args:
        data: A string of characters representing a full Verhoeff code
            with a question mark for a missing character

    Returns:
        str: The missing value that should’ve been where the question mark was

    Examples:
        >>> from checkdigit import verhoeff
        >>> verhoeff.missing("23?3")
        '6'
        >>> verhoeff.missing("999?")
        '8'
        >>> verhoeff.missing("123")
        'Invalid'
    """
    return missing_template(data, "verhoeff")
