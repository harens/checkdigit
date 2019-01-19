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

from checkdigit import isbn

number_success = 0
number_failed = 0
total_tests = 0


# Test function
def test(function, value):
    global total_tests
    total_tests += 1
    linenum = str(sys._getframe(1).f_lineno)
    did_pass = function == value
    if did_pass:
        print("✅ Line {0} Succeeded".format(linenum))
        global number_success
        number_success += 1
    else:
        print("")
        print("❌ Line {0} failed".format(linenum))
        print("Program Output:", function)
        print("Expected Output:", value)
        global number_failed
        number_failed += 1
        print("")


test(isbn.evenparity("0110"), "01100")
test(isbn.evenparity("0"), "00")
test(isbn.evenparity("01101"), "011011")

test(isbn.isbn10calculate("006196436"), "0")
test(isbn.isbn10calculate("190592105"), "5")
test(isbn.isbn10calculate("043942089"), "X")

test(isbn.isbn10check("0198526636"), True)

test(isbn.isbn13calculate("012345678912"), "8")

print("")
if number_failed == 0:
    print("Out of {0} tests, all succeeded".format(total_tests))
elif number_success == 0:
    print("Out of {0} tests, all failed".format(total_tests))
    exit(1)
else:
    print(
        "Out of {0} tests, {1} succeeded and {2} failed".format(
            total_tests, number_success, number_failed
        )
    )
    # Success rate rounded to 2 d.p.
    print(
        "This gives a success rate of {0}%".format(
            round((number_success / total_tests) * 100), 2
        )
    )
    exit(1)
