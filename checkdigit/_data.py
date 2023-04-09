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

"""Generic helper methods.

This module contains functions that help to format data so that it can be interpreted easier.
It also helps deal with type hints in different versions, as well as with general refactoring.
"""

import importlib
import sys
from typing import Any

# ------------------------------------------------------------------------
# DATA CLEANSING FUNCTIONS
# ------------------------------------------------------------------------


def cleanse(data: str) -> str:
    """Removes Hyphens and Spaces so that data can be parsed."""
    return data.replace("-", "").replace(" ", "")


def convert(digit: int, isbn10: bool = True) -> str:
    """Converts digits to strings and replaces 10 and 11.

    Args:
        digit: The code to be modified.
        isbn10: Whether the code is ISBN-10 or not.
    """
    if digit == 10:
        return "X" if isbn10 else "0"
    return "0" if digit == 11 else str(digit)


# ------------------------------------------------------------------------
# PYTHON TYPING IMPORTS
# ------------------------------------------------------------------------

# Deals with typing module being depreciated
PYTHON_AT_LEAST_3_9 = sys.version_info >= (3, 9)

# Use typing module below python 3.9
# Initialised first with Any to make mypy happy
TupleType: Any = None

# Don't count code coverage since different python versions
# won't run different parts of code
if PYTHON_AT_LEAST_3_9:  # pragma: no cover
    TupleType = tuple
else:  # pragma: no cover
    from typing import Tuple

    TupleType = Tuple


# ------------------------------------------------------------------------
# REFACTORED MISSING METHOD
# ------------------------------------------------------------------------
# Inspired by https://stackoverflow.com/a/48981829


# Pytest coverage not applicable since these are just types.
class ModuleInterface:  # pragma: no cover
    """Sets the types of the various functions that are imported by missing_template."""

    # The data parameter isn't used, although is required to set the type.
    # pylint: disable=unused-argument

    # A body of the function isn't required, since we're just mimicking the types.
    # Hence get mypy to ignore the warning

    @staticmethod
    def validate(data: str) -> bool:  # type: ignore[empty-body]
        """Validates check digits in a full block of data.

        Args:
            data: A string of data representing a full code

        Returns:
            bool: A boolean representing whether the data is valid or not.
        """

    @staticmethod
    def calculate(data: str) -> str:  # type: ignore[empty-body]
        """Calculates check digits for a block of data.

        Args:
            data: A block of data with a missing check digit

        Returns:
            str: The missing check digit
        """


def import_module_with_interface(module: str) -> ModuleInterface:
    """Imports the module, and sets its type to ModuleInterface to play nice with mypy.

    Args:
        module: The checkdigit module to import

    Returns:
        ModuleInterface: The imported module with the custom validate and calculate types.
    """
    # Type ignore since the type is being reassigned to ModuleInterface
    return importlib.import_module(f"checkdigit.{module}")  # type: ignore


def missing_template(data: str, module: str) -> str:
    """This acts as a general template for the "missing digit" methods.

    Many of the "missing" methods have the same general format.
    i.e. brute force all the digits from 0-9. This template puts
    all the logic into one place.

    This also has the advantage that the docstrings of the original
    missing methods are maintained.

    Args:
        data: A string of characters representing a full code
            with a question mark representing a missing character
        module: The type of code (e.g. isbn, crc, etc). This is
            imported from the checkdigit folder

    Returns:
        str: The missing value that should've been where the question mark was
    """
    # Imports the relevant module for the data type
    data_type = import_module_with_interface(module)

    # We already have an efficient method for the check digit
    if data[-1] == "?":
        # Remove question mark check digit
        return data_type.calculate(data[:-1])

    # We've dealt with the check digit, so X can't be an option
    # Brute force all the possible numbers (0-9 inclusive)
    for option in (data.replace("?", str(i)) for i in range(10)):
        # Validate the new option
        if data_type.validate(option):
            # Replace question mark with new value
            return option[data.index("?")]
    return "Invalid"
