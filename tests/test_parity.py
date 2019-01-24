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

import sys
import time
from config import test

sys.path.append("../")  # Go back a directory
from checkdigit import parity

# Times all test functions
start_time = time.time()

# TEST FUNCTION FORMAT
# First Parameter => Function Output
# Second Parameter => Expected Output
# Third Parameter => Test number/Test name

test(parity.evenparity("0110"), "01100", "evenparity (1)")
test(parity.evenparity("0"), "00", "evenparity (2)")
test(parity.evenparity("01101"), "011011", "evenparity (3)")

test(parity.oddparity("0110"), "01101", "oddparity (1)")
test(parity.oddparity("0"), "01", "oddparity (2)")
test(parity.oddparity("01101"), "011010", "oddparity (3)")

# Overall Time Completion
final_time = time.time()


# Imported by tests.py to determine overall time completion
def parity_time():
    return final_time - start_time
