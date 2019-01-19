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

sys.path.append("../")  # Go back a directory
from checkdigit import isbn

number_success = 0
number_failed = 0
total_tests = 0


# Test function (Credit to spscah)
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


start_time = time.time()

test(isbn.evenparity("0110"), "01100")
test(isbn.evenparity("0"), "00")
test(isbn.evenparity("01101"), "011011")

test(isbn.isbn10calculate("006196436"), "0")
test(isbn.isbn10calculate("190592105"), "5")
test(isbn.isbn10calculate("043942089"), "X")

test(isbn.isbn10check("0198526636"), True)

test(isbn.isbn13calculate("012345678912"), "8")

# For ISBN-10
test(isbn.calculate_missing("15688?111X"), "1")
test(isbn.calculate_missing("812071988?"), "3")
test(isbn.calculate_missing("020161586?"), "X")
test(isbn.calculate_missing("?131103628"), "0")
test(isbn.calculate_missing("?86046324X"), "1")
test(isbn.calculate_missing("1?68811306"), "5")
test(isbn.calculate_missing("951?451570"), "4")
test(isbn.calculate_missing("0393020?31"), "2")
test(isbn.calculate_missing("01367440?5"), "9")

finish_time = time.time()
final_time = round(finish_time - start_time, 4)

print("")
if number_failed == 0:
    print(
        "Out of {0} tests, all succeeded in {1} seconds".format(total_tests, final_time)
    )
elif number_success == 0:
    print("Out of {0} tests, all failed in {1} seconds".format(total_tests, final_time))
    exit(1)
else:
    print(
        "Out of {0} tests, {1} succeeded and {2} failed in {3} seconds".format(
            total_tests, number_success, number_failed, final_time
        )
    )
    # Success rate rounded to 2 d.p.
    print(
        "This gives a success rate of {0}%".format(
            round((number_success / total_tests) * 100), 2
        )
    )
    exit(1)
