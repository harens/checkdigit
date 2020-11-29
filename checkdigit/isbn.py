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


def calculate10(data: str) -> str:
    """Calculates ISBN-10 Check Digit

    Args:
        data: A string of 9 characters

    Returns:
        str: The check digit that was missing
    """
    data = cleanse(data)
    total_sum = 0
    multiply_counter = 10
    for item in data:
        total_sum += int(item) * multiply_counter
        multiply_counter -= 1  # Multiplies first digit by 10, second by 9...
    check_digit = 11 - (total_sum % 11)
    return convert(check_digit)


def validate10(data: str) -> bool:
    """Validates ISBN-10

    Args:
        data: A string of characters representing a full ISBN-10 code

    Returns:
        bool: A boolean representing whether the check digit validates the data or not

    """
    data = cleanse(data)
    return calculate10(data[:-1]) == data[-1]


def calculate13(data: str, barcode: str = "isbn") -> str:
    """Calculates ISBN-13 Check Digit

    Args:
        data: A string of 12 characters
        barcode: The type of code (either isbn or upc)

    Returns:
        str: The check digit that was missing
    """
    data = cleanse(data)
    mod_number = 0 if barcode == "isbn" else 1
    total_sum = 0
    position_counter = 1  # 1 based indexing for data
    for item in data:
        digit = int(item)
        if position_counter % 2 == mod_number:
            total_sum += digit * 3  # Multiplies by 3 if position is even
        else:
            total_sum += digit
        position_counter += 1
    final_value = 10 - (total_sum % 10)
    return convert(final_value, barcode)


def validate13(data: str) -> bool:
    """Validates ISBN-13

    Args:
        data: A string of characters representing a full ISBN-13 code

    Returns:
        bool: A boolean representing whether the check digit validates the data

    """
    data = cleanse(data)
    return calculate13(data[:-1]) == data[-1]


def missing(data: str) -> str:
    """Calculates a missing digit in an ISBN Code

    Args:
        data: A string of characters representing a full ISBN code with a question mark representing a missing character

    Returns:
        str: The missing value that should've been where the question mark was

    """
    data = cleanse(data)
    for poss_digit in range(11):  # Brute Force the 11 options
        option = convert(poss_digit)
        # Depending on the size of the data, the relevant validating function tests it with the generated number
        # If this fails, the next number is tried
        if (len(data) == 10 and validate10(data.replace("?", option))) or (
            len(data) == 13 and validate13(data.replace("?", option))
        ):
            return option
    return "Invalid"
