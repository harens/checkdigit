# checkdigit
[![Travis build status](https://img.shields.io/travis/com/harens/checkdigit.svg?style=for-the-badge)](https://travis-ci.com/harens/checkdigit) 
[![Latest PyPi release version number](https://img.shields.io/pypi/v/checkdigit.svg?logoColor=violet&style=for-the-badge)](https://pypi.org/project/checkdigit/)
[![PyPi format](https://img.shields.io/pypi/format/checkdigit.svg?style=for-the-badge)](https://pypi.org/project/checkdigit/)
[![Current state (Alpha/Beta/Stable etc.)](https://img.shields.io/pypi/status/checkdigit.svg?style=for-the-badge)](https://pypi.org/project/checkdigit/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/checkdigit.svg?style=for-the-badge)](https://pypi.org/project/checkdigit/)
<br>
<br>
*Checking digits with a digit!*

<img src="./art/parity.png" alt="Sample Parity" width="433"/> <img src="./art/upc.png" alt="Sample UPC" width="433"/>

<img src="./art/isbn.png" alt="Sample ISBN" width="433"/> <img src="./art/luhn.png" alt="Sample Luhn" width="433"/>

## Installation
```shell
pip install checkdigit
```
Or download the project [here](https://github.com/harens/checkdigit/archive/master.zip)
## Features
- Add a parity digit to a string of binary
- ISBN
    - Validates both ISBN-10 and ISBN-13 Codes
    - Determines Missing Digits
    - Calculates Check Digits
- UPC
    - Evaluates Check Digits
    - Validates UPC Codes
- Luhn
    - Validates Credit Cards, IMEI Numbers, and more!
    - Determines Check Digits


## Tests
The test folder can be found here [here](https://github.com/harens/checkdigit/tree/master/tests)

You can run the tests by running `python tests.py`
## License
This project is licensed under the [GNU General Public License v3.0](https://github.com/harens/checkdigit/blob/master/LICENSE)
