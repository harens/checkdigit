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

"""Parity Validation Functions.

A parity bit is added to the end of a block of binary as a form of data validation.

"""

from checkdigit._data import cleanse

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str, even: bool = True) -> str:
    """Adds a parity bit onto the end of a block of data.

    Args:
        data: A string containing binary digits
        even: Whether to use even or odd parity (defaults to even)

    Returns:
        str: The parity bit of the data

    Examples:
        >>> from checkdigit import parity
        >>> # Even parity
        >>> parity.calculate("0110")
        '0'
        >>> parity.calculate("01101")
        '1'

        >>> # Odd parity
        >>> parity.calculate("01101", False)
        '0'
        >>> parity.calculate("0", False)
        '1'

    """
    data = cleanse(data)
    if (even and not data.count("1") % 2) or (not even and data.count("1") % 2):
        return "0"
    return "1"


def validate(data: str, even: bool = True) -> bool:
    """Validates whether the check digit matches a block of data.

    Args:
        data: A string containing binary digits
        even: Whether to use even or odd parity (defaults to even)

    Returns:
        bool: A boolean representing whether the data is valid or not

    Examples:
        >>> from checkdigit import parity
        >>> # Even parity
        >>> parity.validate("01100")
        True
        >>> parity.validate("01101")
        False

        >>> # Odd parity
        >>> parity.validate("01101", False)
        True
        >>> parity.validate("01100", False)
        False
    """
    data = cleanse(data)
    return calculate(data[:-1], even) == data[-1]


def missing(data: str, even: bool = True) -> str:
    """Calculates a missing digit represented by a question mark.

    Args:
        data: A string containing a question mark representing a missing digit.
        even: Whether to use even or odd parity (defaults to even)

    Returns:
        str: The missing binary digit

    Examples:
        >>> from checkdigit import parity
        >>> # Even parity
        >>> parity.missing("01?00")
        '1'
        >>> parity.missing("01?100")
        '0'

        >>> # Odd parity
        >>> parity.missing("01101?", False)
        '0'
        >>> parity.missing("010010?011", False)
        '1'
    """
    # Same principle as check digit (just not necessarily on the end)
    return calculate(data.replace("?", ""), even)
