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

import checkdigit.parity as parity


class TestCalculate:
    def test_even(self) -> None:
        """Calculate even parity check digit."""
        assert parity.calculate("0110") == "0"
        assert parity.calculate("0") == "0"
        assert parity.calculate("01101") == "1"

    def test_odd(self) -> None:
        """Calculate odd parity check digit."""
        assert parity.calculate("0110", False) == "1"
        assert parity.calculate("0", False) == "1"
        assert parity.calculate("01101", False) == "0"


class TestValidate:
    def test_even(self) -> None:
        """Validate even parity check digit."""
        assert parity.validate("01100")
        assert not parity.validate("01101")

    def test_odd(self) -> None:
        """Validate odd parity check digit."""
        assert parity.validate("01101", False)
        assert not parity.validate("01100", False)


class TestMissing:
    def test_even(self) -> None:
        """Missing parity digit (even)."""
        assert parity.missing("01?00") == "1"
        assert parity.missing("01?100") == "0"
        assert parity.missing("010100?") == "0"

    def test_odd(self) -> None:
        """Missing parity digit (odd)."""
        assert parity.missing("01101?", False) == "0"
        assert parity.missing("01?010", False) == "1"
        assert parity.missing("010010?011", False) == "1"
