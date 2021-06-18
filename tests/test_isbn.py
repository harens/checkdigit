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

from checkdigit import gtin


class TestISBN10:
    def test_calculate(self) -> None:
        """ISBN-10 Check digit."""
        assert gtin.calculate("006196436", True) == "0"
        assert gtin.calculate("190592105", True) == "5"
        assert gtin.calculate("043942089", True) == "X"
        assert gtin.calculate("02345678912", True) == "Invalid"

    def test_validate(self) -> None:
        """Validate ISBN-10."""
        assert gtin.validate("0205080057", True)
        assert gtin.validate("0198526636", True)
        assert gtin.validate("1-56619-909-3", True)
        assert not gtin.validate("01-9323852", True)
        assert not gtin.validate("423423", True)

    def test_missing(self) -> None:
        """Determines missing digit in ISBN 10."""
        assert gtin.missing("15688?111X", True) == "1"
        assert gtin.missing("812071988?", True) == "3"
        assert gtin.missing("020161586?", True) == "X"
        assert gtin.missing("?131103628", True) == "0"
        assert gtin.missing("?86046324X", True) == "1"
        assert gtin.missing("1?68811306", True) == "5"
        assert gtin.missing("951?451570", True) == "4"
        assert gtin.missing("0393020?31", True) == "2"
        assert gtin.missing("01367440?5", True) == "9"


class TestISBN13:
    def test_calculate(self) -> None:
        """Determine ISBN-13 Check Digit."""
        assert gtin.calculate("012345678912", True) == "8"
        assert gtin.calculate("978-1-86197-876", True) == "9"

    def test_validate(self) -> None:
        """Validates ISBN 13 codes."""
        assert gtin.validate("0123456789128", True)
        assert gtin.validate("9781861978769", True)
        assert gtin.validate("9-501101-530003", True)
        assert gtin.validate("978-1-56619-909-4", True)

    def test_missing(self) -> None:
        """Determines missing digit."""
        assert gtin.missing("978186197876?", True) == "9"
        assert gtin.missing("9781?61978769", True) == "8"
        assert gtin.missing("01234567891?8", True) == "2"
        assert gtin.missing("0?23456789128", True) == "1"
        assert gtin.missing("978-074?595823", True) == "7"
        assert gtin.missing("978-074759582?", True) == "3"
        assert gtin.missing("023456789128", True) == "Invalid"
