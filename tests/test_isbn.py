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

test(isbn.isbn13check('0123456789128'), True, 'isbn13check (1)')
test(isbn.isbn13check('9781861978769'), True, 'isbn13check (2)')

test(isbn.calculate_missing("15688?111X"), "1", 'calculate_missing (10a)')
test(isbn.calculate_missing("812071988?"), "3", 'calculate_missing (10b)')
test(isbn.calculate_missing("020161586?"), "X", 'calculate_missing (10c)')
test(isbn.calculate_missing("?131103628"), "0", 'calculate_missing (10d)')
test(isbn.calculate_missing("?86046324X"), "1", 'calculate_missing (10e)')
test(isbn.calculate_missing("1?68811306"), "5", 'calculate_missing (10f)')
test(isbn.calculate_missing("951?451570"), "4", 'calculate_missing (10g)')
test(isbn.calculate_missing("0393020?31"), "2", 'calculate_missing (10h)')
test(isbn.calculate_missing("01367440?5"), "9", 'calculate_missing (10i)')

test(isbn.calculate_missing("978186197876?"), "9", 'calculate_missing (13a)')
test(isbn.calculate_missing("9781?61978769"), "8", 'calculate_missing (13b)')
test(isbn.calculate_missing("01234567891?8"), "2", 'calculate_missing (13c)')
test(isbn.calculate_missing("0?23456789128"), "1", 'calculate_missing (13d)')

finish_time = time.time()

def isbn_time():
    return finish_time - start_time
