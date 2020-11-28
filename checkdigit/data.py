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


def cleanse(data: str) -> str:
    """Removes Hyphens and Spaces so that data can be parsed"""
    return data.replace("-", "").replace(" ", "")


def convert(digit: int, barcode: str = "isbn") -> str:
    """Converts digits to strings and replaces 10"""
    if digit == 10:
        return "X" if barcode == "isbn" else "0"
    return "0" if digit == 11 else str(digit)
