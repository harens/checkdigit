.. image:: https://raw.githubusercontent.com/harens/checkdigit/master/art/logo.png
   :alt: checkdigit logo
   :align: center

|

.. image:: https://img.shields.io/github/workflow/status/harens/checkdigit/Tests?logo=github&style=flat-square
   :alt: GitHub Tests status

.. image:: https://img.shields.io/codecov/c/github/harens/checkdigit?logo=codecov&style=flat-square
   :alt: Codecov

.. image:: https://img.shields.io/pypi/dm/checkdigit?logo=python&logoColor=white&style=flat-square
   :alt: PyPi - Downloads

.. image:: https://img.shields.io/codefactor/grade/github/harens/checkdigit?logo=codefactor&style=flat-square
   :alt: CodeFactor Grade

.. image:: https://img.shields.io/lgtm/grade/python/github/harens/checkdigit?logo=lgtm&style=flat-square
   :alt: LGTM Grade

|

.. image:: https://raw.githubusercontent.com/harens/checkdigit/master/art/demo.gif
   :alt: checkdigit example gif
   :align: center

**checkdigit** is a pure Python library built for identification numbers.
You want to validate a credit card number, or maybe even calculate a missing digit on an ISBN code?
We've got you covered 😎.

Want to know more? Check out the `API Reference and documentation <https://checkdigit.readthedocs.io/en/latest/reference.html>`_!

Installation
------------

`MacPorts <https://ports.macports.org/port/py-checkdigit/summary>`_ 🍎
*************************************************************************

.. code-block::

    sudo port install py-checkdigit

`PyPi <https://pypi.org/project/checkdigit/>`_ 🐍
**************************************************

.. code-block::

    pip install checkdigit

✨ Features
------------

* `PEP 561 compatible <https://www.python.org/dev/peps/pep-0561>`_, with built in support for type checking.
* Capable of calculating missing digits or validating a block of data.
* Extensive in-code comments and docstrings to explain how it works behind the scenes. 🪄

✅ Supported Formats
---------------------

* Even and odd binary parity
* Bookland
* CRC (credit to `@sapieninja <https://github.com/sapieninja>`_)
* EAN-13
* GS1 (credit to `@OtherBarry <https://github.com/OtherBarry>`_)
* ISBN-10
* ISBN-13
* Luhn
* UPC-A

For each of these formats, we provide functions to validate them and calculate missing digits.

Do you have any formats that you'd like to see supported? 🤔 Feel free to raise an issue,
or even to send a pull request!

🔨 Contributing
---------------

- Issue Tracker: `<https://github.com/harens/checkdigit/issues>`_
- Source Code: `<https://github.com/harens/checkdigit>`_

Any change, big or small, that you think can help improve this project is more than welcome 🎉.

As well as this, feel free to open an issue with any new suggestions or bug reports. Every contribution is appreciated.

🏗 Setup
*********

First, fork the project to your account. Then, run the following with your GitHub handle in place of
:code:`INSERT_GITHUB_NAME`:

.. code-block:: console

    git clone https://github.com/INSERT_GITHUB_NAME/checkdigit
    poetry install && poetry shell
    pre-commit install


🏛 Project structure
********************

..
   Credit for file structure: https://stackoverflow.com/a/38819161

::

    checkdigit
    ├── scripts
    │   ├── format.sh
    │   └── tests.sh
    ├── checkdigit
    │   ├── gs1.py
    │   ├── isbn.py
    │   ├── luhn.py
    │   └── etc.
    └── tests

Each new format goes into a separate file which is named accordingly. Similar formats (e.g. ISBN-10 and ISBN-13)
should go in the same file.

Before submitting any new changes, please run the :code:`format.sh` and :code:`tests.sh` scripts beforehand. Thank you :)

📚 Building the Docs
*********************

The documentation can be found in :code:`docs/source`.

We can use `sphinx-autobuild <https://github.com/executablebooks/sphinx-autobuild>`_ to continuously rebuild the docs when changes are made.

.. code-block:: console

    sphinx-autobuild docs/source docs/_build/html

🎪 File structure
*****************

Each of the Python files follow the same general format:

.. code-block:: python

    # License + File docstring

    from checkdigit._data import cleanse, convert


    def calculate(data: str) -> str:
        """Determines check digit.

        Args:
            data: A string of data missing a check digit

        Returns:
            str: The single missing check digit (not the whole block of data)
        """
        # This helps to deal with user formatting inconsistencies
        # e.g. spaces, hyphens, etc.
        data = cleanse(data)

        # Deals with 10 or 11 being the possible check digit
        return convert(...)


    def validate(data: str) -> bool:
        """Validates a block of data from the check digit.

        Args:
            data: A string representing a full block of data

        Returns:
            bool: A boolean representing whether the data is valid or not
        """
        data = cleanse(data)

        # Remove the check digit and see if it matches
        return calculate(data[:-1]) == data[-1]


    def missing(data: str) -> str:
        """Returns the missing digit from a block of data.

        Args:
            data: A string with a question mark in the place of a missing digit.

        Returns:
            A string representing the missing digit (not the whole block of data)
        """
        data = cleanse(data)

        return ...

For similar data formats, the names can be adjusted accordingly (e.g. :code:`validate10` for ISBN-10 and :code:`validate13` for ISBN-13).

📙 License
-----------

This project is licensed under `GPL-3.0-or-later <https://github.com/harens/checkdigit/blob/master/LICENSE>`_.
