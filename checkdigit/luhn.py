# /usr/bin/env python

# This file is part of checkdigit.

# Types-and-Variables is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# checkdigit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with checkdigit.  If not, see <http://www.gnu.org/licenses/>.


def luhn_calculate(data):
    position_counter = 1
    total_sum = 0
    for item in data[::-1]:  # Reverses String
        item = int(item)
        if position_counter % 2 == 1:
            add_value = item * 2
            if add_value > 9:
                for number in str(add_value):  # Adds individual digits together
                    total_sum += int(number)
            else:
                total_sum += add_value
        else:
            total_sum += item
        position_counter += 1
    final_result = 10 - (total_sum % 10)
    if final_result == 10:
        return '0'
    return str(final_result)


def luhn_validate(data):
    return luhn_calculate(data[:-1]) == data[-1]
