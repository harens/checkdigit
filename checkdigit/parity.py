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


# WARNING: Data beginning with 0 must be as a string due to PEP 3127

def evenparity(data):
    data = str(data).replace('-', '').replace(' ', '')  # Removes Hyphens and Spaces
    if data.count("1") % 2 == 0:
        return data + "0"
    return data + "1"


def oddparity(data):
    data = str(data).replace('-', '').replace(' ', '')  # Removes Hyphens and Spaces
    if data.count("1") % 2 == 0:
        return data + "1"
    return data + "0"
