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

from checkdigit import crc


def test_calculate() -> None:
    """CRC generating correct check parts."""
    assert crc.calculate("1010", "1011") == "011"
    assert crc.calculate("010101", "1101") == "111"
    assert crc.calculate("1111011011", "1101001") == "010100"
    assert crc.calculate("100100011101", "111") == "11"
    assert crc.calculate("100110010100111101111101", "11010111101") == "0010001100"


def test_validate() -> None:
    """Validate CRC data."""
    assert crc.validate("1010101", "101")
    assert crc.validate("1001100101001111011111010010001100", "11010111101")
    assert not crc.validate("1000101", "101")
    assert not crc.validate("1001100101001111011111010010001110", "11010111101")


def test_missing() -> None:
    """Determines missing values from CRC data."""
    assert crc.missing("10?110010100111?0?1111?10010?011?0", "11010111101") == "011000"
    assert crc.missing("?1111111101", "1101") == "1"
    assert crc.missing("101101001", "11101") == "Invalid"
    assert crc.missing("?????????", "111") == "Invalid"
    assert crc.missing("?1111111001", "1101") == "Invalid"
