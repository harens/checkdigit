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

start_time = time.time()

sys.path.append("../")  # Go back a directory
from checkdigit import upc

test(upc.upcCalculate("17593487596") == "0")
test(upc.upcCalculate("64161295255") == "6")
test(upc.upcCalculate("69861509878") == "1")
test(upc.upcCalculate("73799324006") == "8")
test(upc.upcCalculate("69645331139") == "0")

finish_time = time.time()

def upc_time():
    return finish_time - start_time
