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


# Calculates ISBN-10 Check Digits
def isbn10calculate(data):
    total_sum = 0
    multiply_counter = 10
    for item in data:
        total_sum += int(item) * multiply_counter
        multiply_counter -= 1  # Multiplies first digit by 10, second by 9...
    check_digit = 11 - (total_sum % 11)
    if check_digit == 10:
        return "X"
    elif check_digit == 11:
        return "0"
    return str(check_digit)


# Validates ISBN-10
def isbn10check(data):
    return (
        isbn10calculate(data[:9]) == data[-1]
    )  # Determines if calculated Check Digit of the data is the last digit given


def isbn13calculate(data, function_name="isbn"):
    if function_name == "isbn":
        mod_number = 0
    else:
        mod_number = 1  # Used for UPC
    total_sum = 0
    position_counter = 1  # 1 based indexing for data
    for item in data:
        item = int(item)
        if position_counter % 2 == mod_number:
            total_sum += item * 3  # Multiplies by 3 if position is even
        else:
            total_sum += item
        position_counter += 1
    final_value = 10 - (total_sum % 10)
    if final_value == 10 and function_name != "isbn":
        return "0"  # X is not a valid option for UPCs
    elif final_value == 10:
        return "X"  # X is a vaild option for the last digit of ISBNs
    return str(final_value)


def isbn13check(data):
    return (
        isbn13calculate(data[:12]) == data[-1]
    )  # Determines if calculated Check Digit of the data is the last digit given


def calculate_missing(data):
    for poss_digit in range(0, 11):  # Brute Force the 11 options
        if poss_digit == 10:
            poss_digit = "X"  # '10' as a single digit is X
        # Depending on the size of the data, the relevant validating function tests it with the generated number
        # If this fails, the next number is tried
        if len(data) == 10 and isbn10check(data.replace("?", str(poss_digit))):
            return str(poss_digit)
        elif len(data) == 13 and isbn13check(data.replace("?", str(poss_digit))):
            return str(poss_digit)
