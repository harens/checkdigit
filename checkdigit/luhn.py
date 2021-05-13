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

"""Luhn Validation Functions.

The luhn algorithm has a variety of applications, including in credit cards and IMEI numbers.

For more information, please look at the wiki page for this module:
https://github.com/harens/checkdigit/wiki/💳-Luhn

"""

from checkdigit._data import cleanse

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str) -> str:
    """Calculates the luhn check digit.

    Args:
        data: A block of data without the check digit

    Returns:
        str: A string representing the missing check digit

    """
    data = cleanse(data)
    # Double every other digit, starting from the final digit backwards
    # i.e. double 0th digit, 2nd, 4th, ...
    double_digits = (
        int(element) if index % 2 else int(element) * 2
        for index, element in enumerate(data[::-1])
    )
    # For digits with more than one digit, sum the digits together
    # The maximum is 9*2 = 18. This divmod method will work <100
    sum_digits = sum(sum(divmod(i, 10)) for i in double_digits)
    # Mod 10 returns 0-9 (not 10 or 11)
    # Hence convert method not required (faster to use str)
    return str((sum_digits * 9) % 10)


def validate(data: str) -> bool:
    """Validates a luhn check digit.

    Args:
        data: A string of characters representing a full luhn code

    Returns:
        bool: A boolean representing whether the check digit validates the data or not

    """
    data = cleanse(data)
    return (
        calculate(data[:-1]) == data[-1]
    )  # Determines if calculated Check Digit of the data is the last digit given


def missing(data: str) -> str:
    """Calculates a missing digit in a luhn code.

    Args:
        data: A string of characters representing a full luhn code
            with a question mark for a missing character

    Returns:
        str: The missing value that should've been where the question mark was

    """
    data = cleanse(data)
    for poss_digit in range(10):  # Brute Force the 10 options
        if validate(data.replace("?", str(poss_digit))):
            return str(poss_digit)
    return "Invalid"
