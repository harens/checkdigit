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

"""Tests File.

This file contains error404 tests for the checkdigit library.
The various sections are marked by comments e.g. # Even parity.

Test Function Format:
    * First Parameter => Function Output
    * Second Parameter => Expected Output (not required if output is True)

"""

from error404 import test

import checkdigit.isbn as isbn
import checkdigit.luhn as luhn
import checkdigit.parity as parity
import checkdigit.upc as upc
import checkdigit.gs1 as gs1

# Even parity
test(parity.calculate("0110"), "01100")
test(parity.calculate("0"), "00")
test(parity.calculate("01101"), "011011")

# Odd parity
test(parity.calculate("0110", False), "01101")
test(parity.calculate("0", False), "01")
test(parity.calculate("01101", False), "011010")

# ISBN-10 Check digit
test(isbn.calculate10("006196436"), "0")
test(isbn.calculate10("190592105"), "5")
test(isbn.calculate10("043942089"), "X")

# Validate ISBN-10
test(isbn.validate10("0205080057"))
test(isbn.validate10("0198526636"))
test(isbn.validate10("1-56619-909-3"))
test(isbn.validate10("01-9323852"), False)
test(isbn.validate10("423423"), False)

# Determine ISBN-13 Check Digit
test(isbn.calculate13("012345678912"), "8")
test(isbn.calculate13("978-1-86197-876"), "9")

test(isbn.calculate13("501234567890", "upc"), "0")
test(isbn.calculate13("03600029145", "upc"), "2")
test(isbn.calculate13("89268500100", "upc"), "3")

# Validate ISBN-13
test(isbn.validate13("0123456789128"))
test(isbn.validate13("9781861978769"))
test(isbn.validate13("9-501101-530003"))
test(isbn.validate13("978-1-56619-909-4"))

# ISBN-10 Missing Digit
# Must be string due to ? and/or X
test(isbn.missing("15688?111X"), "1")
test(isbn.missing("812071988?"), "3")
test(isbn.missing("020161586?"), "X")
test(isbn.missing("?131103628"), "0")
test(isbn.missing("?86046324X"), "1")
test(isbn.missing("1?68811306"), "5")
test(isbn.missing("951?451570"), "4")
test(isbn.missing("0393020?31"), "2")
test(isbn.missing("01367440?5"), "9")

# ISBN-13 Missing Digit
test(isbn.missing("978186197876?"), "9")
test(isbn.missing("9781?61978769"), "8")
test(isbn.missing("01234567891?8"), "2")
test(isbn.missing("0?23456789128"), "1")
test(isbn.missing("978-074?595823"), "7")
test(isbn.missing("978-074759582?"), "3")
test(isbn.missing("023456789128"), "Invalid")

# Determines Check Digit
test(upc.calculate("17593487596"), "0")
test(upc.calculate("64161295255"), "6")
test(upc.calculate("69861509878"), "1")
test(upc.calculate("73799324006"), "8")
test(upc.calculate("69645331139"), "0")

# Validates UPC Code
test(upc.validate("672792398018"))
test(upc.validate("641612952556"))
test(upc.validate("698615098781"))
test(upc.validate("737993240068"))
test(upc.validate("696453311390"))

test(upc.validate("672792398017"), False)
test(upc.validate("641612952555"), False)
test(upc.validate("698615098782"), False)
test(upc.validate("737993240069"), False)
test(upc.validate("696453311393"), False)

# Determine Check Digit
test(luhn.calculate("53251309870224"), "3")
test(luhn.calculate("601195843045086"), "9")
test(luhn.calculate("543669577125419"), "0")
test(luhn.calculate("436076111511668"), "6")
test(luhn.calculate("37266630277430"), "0")
test(luhn.calculate("91497796683515"), "3")
test(luhn.calculate("10408772972296"), "9")
test(luhn.calculate("950123440000"), "8")

# Validate Data
test(luhn.validate("541756116585277"))
test(luhn.validate("526012730485489"))
test(luhn.validate("515853022176176"))
test(luhn.validate("6011365035868968"))
test(luhn.validate("372098369216316"))
test(luhn.validate("4556098986775827"))
test(luhn.validate("79927398713"))
test(luhn.validate("49927398717"), False)
test(luhn.validate("79927398710"), False)
test(luhn.validate("79927398711"), False)
test(luhn.validate("79927398712"), False)
test(luhn.validate("79927398719"), False)
test(luhn.validate("1234567812345678"), False)
test(luhn.validate("2222222222222222"), False)
test(luhn.validate("111111111111111"), False)
test(luhn.validate("33333333333333"), False)

# Missing Digit
test(luhn.missing("54175611658527?"), "7")
test(luhn.missing("52601273?485489"), "0")
test(luhn.missing("515853022?76176"), "1")
test(luhn.missing("?72098369216316"), "3")
test(luhn.missing("78369216316"), "Invalid")

# Determine Check Digit
test(gs1.calculate("9894552"), "8")
test(gs1.calculate("7384553"), "9")
test(gs1.calculate("6095011"), "6")
test(gs1.calculate("24497088432"), "5")
test(gs1.calculate("97379430662"), "0")
test(gs1.calculate("82778161993"), "7")
test(gs1.calculate("992802203539"), "2")
test(gs1.calculate("484614659301"), "5")
test(gs1.calculate("508533792649"), "5")
test(gs1.calculate("1268148598279"), "8")
test(gs1.calculate("2943824610504"), "6")
test(gs1.calculate("2839112640382"), "7")
test(gs1.calculate("4314789452907127"), "9")
test(gs1.calculate("6427894156382299"), "3")
test(gs1.calculate("9770280892681722"), "8")
test(gs1.calculate("08408575249213173"), "1")
test(gs1.calculate("84668430275000727"), "9")
test(gs1.calculate("67368623738347505"), "1")

# Determine Check Digit
test(gs1.validate("45649554"))
test(gs1.validate("53089328"))
test(gs1.validate("026229133848"))
test(gs1.validate("791364257635"))
test(gs1.validate("1396057123946"))
test(gs1.validate("3832293285225"))
test(gs1.validate("97781402171203"))
test(gs1.validate("02146346514943"))
test(gs1.validate("25020757663329968"))
test(gs1.validate("82648071988131734"))
test(gs1.validate("321609478518371973"))
test(gs1.validate("961552634342856982"))
test(gs1.validate("97673485"), False)
test(gs1.validate("52186777"), False)
test(gs1.validate("548785535769"), False)
test(gs1.validate("753963090728"), False)
test(gs1.validate("3293497160526"), False)
test(gs1.validate("6806652313775"), False)
test(gs1.validate("02370607330031"), False)
test(gs1.validate("52262887213914"), False)
test(gs1.validate("83494889067993460"), False)
test(gs1.validate("93976703183564468"), False)
test(gs1.validate("501469249184000304"), False)
test(gs1.validate("224245438987081447"), False)

# Missing Digit
test(gs1.missing("?8945528"), "9")
test(gs1.missing("7?845539"), "3")
test(gs1.missing("60?50116"), "9")
test(gs1.missing("244?70884325"), "9")
test(gs1.missing("9737?4306620"), "9")
test(gs1.missing("82778?619937"), "1")
test(gs1.missing("992802?035392"), "2")
test(gs1.missing("4846146?93015"), "5")
test(gs1.missing("50853379?6495"), "2")
test(gs1.missing("126814859?2798"), "8")
test(gs1.missing("2943824610?046"), "5")
test(gs1.missing("28391126403?27"), "8")
test(gs1.missing("431478945290?1279"), "7")
test(gs1.missing("6427894156382?993"), "2")
test(gs1.missing("97702808926817?28"), "2")
test(gs1.missing("084085752492131?31"), "7")
test(gs1.missing("846684302750007275"), "Invalid")
test(gs1.missing("?73686237383475059"), "0")
