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

from checkdigit.data import cleanse, convert


# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str) -> str:
    """Calculates the luhn check digit

    Args:
        data: A block of data without the check digit

    Returns:
        str: A string representing the missing check digit

    """
    data = cleanse(data)
    position_counter = 1  # 1-based indexing
    total_sum = 0
    for item in data[::-1]:  # Reverses String
        digit = int(item)
        if position_counter % 2:  # If position number is odd with reversed string
            add_value = digit * 2
            if add_value > 9:
                for number in str(add_value):  # Adds individual digits together
                    total_sum += int(number)
            else:
                total_sum += add_value
        else:
            total_sum += digit
        position_counter += 1
    return convert(10 - (total_sum % 10), "luhn")


def validate(data: str) -> bool:
    """Validates a luhn check digit

    Args:
        data: A string of characters representing a full luhn code

    Returns:
        bool: A boolean representing if the check digit validates the data

    """
    data = cleanse(data)
    return (
        calculate(data[:-1]) == data[-1]
    )  # Determines if calculated Check Digit of the data is the last digit given


def missing(data: str) -> str:
    """Calculates a missing digit in a luhn code

    Args:
        data: A string of characters representing a full luhn code with a question mark for a missing character

    Returns:
        str: The missing value that should be where the question mark is

    """
    data = cleanse(data)
    for poss_digit in range(10):  # Brute Force the 10 options
        if validate(data.replace("?", str(poss_digit))):
            return str(poss_digit)
    return "Invalid"
