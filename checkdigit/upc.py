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

from checkdigit import isbn

# ISBN calculations are very similar to that of UPC
# The only major difference is that the ODD instead of even placed digits are multiplied by 3


def upc_calculate(data):
    return isbn.isbn13calculate(data, "upc")


def upc_check(data):
    return (
        upc_calculate(data[:11]) == data[-1]
    )  # Determines if calculated Check Digit of the data is the last digit given
