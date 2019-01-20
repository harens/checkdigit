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

# This file contains variables/functions required across multiple files

import sys

number_success = 0
number_failed = 0
total_tests = 0


# Credit to spscah
def test(function, value, function_name):
    if 'parity' in function_name:
        file_name = 'test_parity.py'
    else:
        file_name = 'test_isbn'
    global total_tests
    total_tests += 1
    linenum = str(sys._getframe(1).f_lineno)
    did_pass = function == value
    if did_pass:
        print("✅ {0} Succeeded".format(function_name))
        global number_success
        number_success += 1
    else:
        print("")
        print("❌ {0} failed at line {1} in {2}".format(function_name, linenum, file_name))
        print("Program Output:", function)
        print("Expected Output:", value)
        global number_failed
        number_failed += 1
        print("")


def final_output(time):
    time = round(time, 4)
    print("")
    if number_failed == 0:
        print(
            "Out of {0} tests, all succeeded in {1} seconds".format(total_tests, time)
        )
    elif number_success == 0:
        print("Out of {0} tests, all failed in {1} seconds".format(total_tests, time))
        exit(1)
    else:
        print(
            "Out of {0} tests, {1} succeeded and {2} failed in {3} seconds".format(
                total_tests, number_success, number_failed, time
            )
        )
        # Success rate rounded to 2 d.p.
        print(
            "This gives a success rate of {0}%".format(
                round((number_success / total_tests) * 100), 2
            )
        )
        exit(1)
