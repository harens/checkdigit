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

For more information, please look at the wiki page for this module:
https://github.com/harens/checkdigit/wiki/1%EF%B8%8F⃣-Parity-Bits

"""

from checkdigit._data import cleanse

# WARNING: Data beginning with 0 must be as a string due to PEP 3127


def calculate(data: str, even: bool = True) -> str:
    """Adds a parity bit onto the end of a block of data.

    Args:
        data: A string containing binary digits
        even: Whether to use even parity (otherwise uses odd parity)

    Returns:
        str: The original data with the parity bit added to the end
    """
    data = cleanse(data)
    if (even and not data.count("1") % 2) or (not even and data.count("1") % 2):
        return data + "0"
    return data + "1"
