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

import checkdigit.gs1 as gs1


def test_calculate() -> None:
    """Determine check digit."""
    assert gs1.calculate("9894552") == "8"
    assert gs1.calculate("7384553") == "9"
    assert gs1.calculate("6095011") == "6"
    assert gs1.calculate("24497088432") == "5"
    assert gs1.calculate("97379430662") == "0"
    assert gs1.calculate("82778161993") == "7"
    assert gs1.calculate("992802203539") == "2"
    assert gs1.calculate("484614659301") == "5"
    assert gs1.calculate("508533792649") == "5"
    assert gs1.calculate("1268148598279") == "8"
    assert gs1.calculate("2943824610504") == "6"
    assert gs1.calculate("2839112640382") == "7"
    assert gs1.calculate("4314789452907127") == "9"
    assert gs1.calculate("6427894156382299") == "3"
    assert gs1.calculate("9770280892681722") == "8"
    assert gs1.calculate("08408575249213173") == "1"
    assert gs1.calculate("84668430275000727") == "9"
    assert gs1.calculate("67368623738347505") == "1"


def test_validate() -> None:
    """Validate gs1 code."""
    assert gs1.validate("53089328")
    assert gs1.validate("45649554")
    assert gs1.validate("026229133848")
    assert gs1.validate("791364257635")
    assert gs1.validate("1396057123946")
    assert gs1.validate("3832293285225")
    assert gs1.validate("97781402171203")
    assert gs1.validate("02146346514943")
    assert gs1.validate("25020757663329968")
    assert gs1.validate("82648071988131734")
    assert gs1.validate("321609478518371973")
    assert gs1.validate("961552634342856982")
    assert not gs1.validate("97673485")
    assert not gs1.validate("52186777")
    assert not gs1.validate("548785535769")
    assert not gs1.validate("753963090728")
    assert not gs1.validate("3293497160526")
    assert not gs1.validate("6806652313775")
    assert not gs1.validate("02370607330031")
    assert not gs1.validate("52262887213914")
    assert not gs1.validate("83494889067993460")
    assert not gs1.validate("93976703183564468")
    assert not gs1.validate("501469249184000304")
    assert not gs1.validate("224245438987081447")


def test_missing() -> None:
    """Calculate missing digit."""
    assert gs1.missing("?8945528") == "9"
    assert gs1.missing("7?845539") == "3"
    assert gs1.missing("60?50116") == "9"
    assert gs1.missing("244?70884325") == "9"
    assert gs1.missing("9737?4306620") == "9"
    assert gs1.missing("82778?619937") == "1"
    assert gs1.missing("992802?035392") == "2"
    assert gs1.missing("4846146?93015") == "5"
    assert gs1.missing("50853379?6495") == "2"
    assert gs1.missing("126814859?2798") == "8"
    assert gs1.missing("2943824610?046") == "5"
    assert gs1.missing("28391126403?27") == "8"
    assert gs1.missing("431478945290?1279") == "7"
    assert gs1.missing("6427894156382?993") == "2"
    assert gs1.missing("97702808926817?28") == "2"
    assert gs1.missing("084085752492131?31") == "7"
    assert gs1.missing("846684302750007275") == "Invalid"
    assert gs1.missing("?73686237383475059") == "0"
