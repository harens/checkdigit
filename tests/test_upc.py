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


def test_calculate() -> None:
    """Determines Check Digit."""
    assert gtin.calculate("17593487596") == "0"
    assert gtin.calculate("64161295255") == "6"
    assert gtin.calculate("69861509878") == "1"
    assert gtin.calculate("73799324006") == "8"
    assert gtin.calculate("69645331139") == "0"


class TestValidate:
    def test_positive(self) -> None:
        """The UPC code is valid."""
        assert gtin.validate("672792398018")
        assert gtin.validate("641612952556")
        assert gtin.validate("698615098781")
        assert gtin.validate("737993240068")
        assert gtin.validate("696453311390")

    def test_negative(self) -> None:
        """The UPC code is invalid."""
        assert not gtin.validate("672792398017")
        assert not gtin.validate("641612952555")
        assert not gtin.validate("698615098782")
        assert not gtin.validate("737993240069")
        assert not gtin.validate("696453311393")
