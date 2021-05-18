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

import checkdigit.upc as upc


def test_calculate() -> None:
    """Determines Check Digit."""
    assert upc.calculate("17593487596") == "0"
    assert upc.calculate("64161295255") == "6"
    assert upc.calculate("69861509878") == "1"
    assert upc.calculate("73799324006") == "8"
    assert upc.calculate("69645331139") == "0"


class TestValidate:
    def test_positive(self) -> None:
        """The UPC code is valid."""
        assert upc.validate("672792398018")
        assert upc.validate("641612952556")
        assert upc.validate("698615098781")
        assert upc.validate("737993240068")
        assert upc.validate("696453311390")

    def test_negative(self) -> None:
        """The UPC code is invalid."""
        assert not upc.validate("672792398017")
        assert not upc.validate("641612952555")
        assert not upc.validate("698615098782")
        assert not upc.validate("737993240069")
        assert not upc.validate("696453311393")
