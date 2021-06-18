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

from checkdigit import isbn


class TestISBN10:
    def test_calculate(self) -> None:
        """ISBN-10 Check digit."""
        assert isbn.calculate("006196436") == "0"
        assert isbn.calculate("190592105") == "5"
        assert isbn.calculate("043942089") == "X"
        assert isbn.calculate("02345678912") == "Invalid"

    def test_validate(self) -> None:
        """Validate ISBN-10."""
        assert isbn.validate("0205080057")
        assert isbn.validate("0198526636")
        assert isbn.validate("1-56619-909-3")
        assert not isbn.validate("01-9323852")
        assert not isbn.validate("423423")

    def test_missing(self) -> None:
        """Determines missing digit in ISBN 10."""
        assert isbn.missing("15688?111X") == "1"
        assert isbn.missing("812071988?") == "3"
        assert isbn.missing("020161586?") == "X"
        assert isbn.missing("?131103628") == "0"
        assert isbn.missing("?86046324X") == "1"
        assert isbn.missing("1?68811306") == "5"
        assert isbn.missing("951?451570") == "4"
        assert isbn.missing("0393020?31") == "2"
        assert isbn.missing("01367440?5") == "9"


class TestISBN13:
    def test_calculate(self) -> None:
        """Determine ISBN-13 Check Digit."""
        assert isbn.calculate("012345678912") == "8"
        assert isbn.calculate("978-1-86197-876") == "9"

    def test_validate(self) -> None:
        """Validates ISBN 13 codes."""
        assert isbn.validate("0123456789128")
        assert isbn.validate("9781861978769")
        assert isbn.validate("9-501101-530003")
        assert isbn.validate("978-1-56619-909-4")

    def test_missing(self) -> None:
        """Determines missing digit."""
        assert isbn.missing("978186197876?") == "9"
        assert isbn.missing("9781?61978769") == "8"
        assert isbn.missing("01234567891?8") == "2"
        assert isbn.missing("0?23456789128") == "1"
        assert isbn.missing("978-074?595823") == "7"
        assert isbn.missing("978-074759582?") == "3"
        assert isbn.missing("023456789128") == "Invalid"
