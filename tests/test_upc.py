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

test(upc.upc_calculate("17593487596"), "0", "upc_calculate (1)")
test(upc.upc_calculate("64161295255"), "6", "upc_calculate (2)")
test(upc.upc_calculate("69861509878"), "1", "upc_calculate (3)")
test(upc.upc_calculate("73799324006"), "8", "upc_calculate (4)")
test(upc.upc_calculate("69645331139"), "0", "upc_calculate (5)")

test(upc.upc_check("672792398018"), True, "upc_check(1)")
test(upc.upc_check("641612952556"), True, "upc_check(2)")
test(upc.upc_check("698615098781"), True, "upc_check(3)")
test(upc.upc_check("737993240068"), True, "upc_check(4)")
test(upc.upc_check("696453311390"), True, "upc_check(5)")
test(upc.upc_check("672792398017"), False, "upc_check(6)")
test(upc.upc_check("641612952555"), False, "upc_check(7)")
test(upc.upc_check("698615098782"), False, "upc_check(8)")
test(upc.upc_check("737993240069"), False, "upc_check(9)")
test(upc.upc_check("696453311393"), False, "upc_check(10)")

finish_time = time.time()


def upc_time():
    return finish_time - start_time
