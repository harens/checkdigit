# checkdigit

A check digit library for data validation.
  
| Test Status | [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/harens/checkdigit/Tests?logo=github&style=flat-square)](https://github.com/harens/checkdigit/actions) [![Codecov](https://img.shields.io/codecov/c/github/harens/checkdigit?style=flat-square)](https://codecov.io/gh/harens/checkdigit)  |
|:--|:--|
| __Version Info__ | [![PyPI](https://img.shields.io/pypi/v/checkdigit?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/checkdigit/) [![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/harens/checkdigit?logo=github&style=flat-square)](https://github.com/harens/checkdigit/releases) [![PyPI - Downloads](https://img.shields.io/pypi/dm/checkdigit?logo=python&logoColor=white&style=flat-square)](https://pypi.org/project/checkdigit/) |
| __Code Analysis__ |[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/harens/checkdigit?logo=code%20climate&style=flat-square)](https://codeclimate.com/github/harens/checkdigit) [![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/harens/checkdigit?logo=codefactor&style=flat-square)](https://www.codefactor.io/repository/github/harens/checkdigit) [![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/harens/checkdigit?logo=lgtm&style=flat-square)](https://lgtm.com/projects/g/harens/checkdigit/)|

## 🔨 Installation

```shell
pip install checkdigit
```

Or download the project [here](https://github.com/harens/checkdigit/archive/master.zip).

## ✨ Features

* Contains various functions relating to __Luhn, ISBN, UPC and many other codes__.
* Extensive __in-code comments and docstrings__ to explain how the functions work.
* Written in __pure Python__ with __no dependencies__ required to run the program.

Check out the [documentation](https://github.com/harens/checkdigit/wiki) for more details on how to use the library.

## 🏗️ Contributing

Any change, big or small, that you think can help improve this project is more than welcome 🎉.

As well as this, feel free to open an issue with any new suggestions or bug reports. Every contribution is valued.

For smaller tasks (that are still really appreciated 😃), be sure to check the [good first issue](https://github.com/harens/checkdigit/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) tag.

## 💻 Setup

Clone the project and install the dev dependencies:

```shell
git clone https://github.com/harens/checkdigit
cd checkdigit
poetry install
```

If you want to send a PR, please run the following:

```bash
bash ./scripts/format.sh # Format files
bash ./scripts/tests.sh  # Run tests

# NB shellcheck is not installed by poetry
shellcheck scripts/*.sh
```

## 📒 License

This project is licensed under [GPL-3.0-or-later](https://github.com/harens/checkdigit/blob/master/LICENSE).
