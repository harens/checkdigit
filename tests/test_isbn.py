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
from checkdigit import isbn

test(isbn.isbn10calculate("006196436"), "0", 'isbn10calculate (1)')
test(isbn.isbn10calculate("190592105"), "5", 'isbn10calculate (2)')
test(isbn.isbn10calculate("043942089"), "X", 'isbn10calculate (3)')

test(isbn.isbn10check("0198526636"), True, 'isbn10check')

test(isbn.isbn13calculate("012345678912"), "8", 'isbn13calculate')

# For ISBN-10
test(isbn.calculate_missing("15688?111X"), "1", 'calculate_missing (1)')
test(isbn.calculate_missing("812071988?"), "3", 'calculate_missing (2)')
test(isbn.calculate_missing("020161586?"), "X", 'calculate_missing (3)')
test(isbn.calculate_missing("?131103628"), "0", 'calculate_missing (4)')
test(isbn.calculate_missing("?86046324X"), "1", 'calculate_missing (5)')
test(isbn.calculate_missing("1?68811306"), "5", 'calculate_missing (6)')
test(isbn.calculate_missing("951?451570"), "4", 'calculate_missing (7)')
test(isbn.calculate_missing("0393020?31"), "2", 'calculate_missing (8)')
test(isbn.calculate_missing("01367440?5"), "9", 'calculate_missing (9)')

finish_time = time.time()

def isbn_time():
    return finish_time - start_time
