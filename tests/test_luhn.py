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

import checkdigit.luhn as luhn


def test_calculate() -> None:
    """Determine check digits."""
    assert luhn.calculate("53251309870224") == "3"
    assert luhn.calculate("601195843045086") == "9"
    assert luhn.calculate("543669577125419") == "0"
    assert luhn.calculate("436076111511668") == "6"
    assert luhn.calculate("37266630277430") == "0"
    assert luhn.calculate("91497796683515") == "3"
    assert luhn.calculate("10408772972296") == "9"
    assert luhn.calculate("950123440000") == "8"


def test_validate() -> None:
    """Validate luhn code."""
    assert luhn.validate("541756116585277")
    assert luhn.validate("526012730485489")
    assert luhn.validate("515853022176176")
    assert luhn.validate("6011365035868968")
    assert luhn.validate("372098369216316")
    assert luhn.validate("4556098986775827")
    assert luhn.validate("79927398713")
    assert not luhn.validate("49927398717")
    assert not luhn.validate("79927398710")
    assert not luhn.validate("79927398711")
    assert not luhn.validate("79927398712")
    assert not luhn.validate("79927398719")
    assert not luhn.validate("1234567812345678")
    assert not luhn.validate("2222222222222222")
    assert not luhn.validate("111111111111111")
    assert not luhn.validate("33333333333333")


def test_missing() -> None:
    """Determine missing digit in luhn code."""
    assert luhn.missing("54175611658527?") == "7"
    assert luhn.missing("52601273?485489") == "0"
    assert luhn.missing("515853022?76176") == "1"
    assert luhn.missing("?72098369216316") == "3"
    assert luhn.missing("78369216316") == "Invalid"
