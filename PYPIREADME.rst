.. image:: https://raw.githubusercontent.com/harens/checkdigit/master/art/logo.png
   :alt: checkdigit logo
   :target: https://github.com/harens/checkdigit
   :align: center

|

.. image:: https://img.shields.io/github/workflow/status/harens/checkdigit/Tests?logo=github&style=flat-square
   :alt: GitHub Tests status
   :target: https://github.com/harens/checkdigit/actions

.. image:: https://img.shields.io/codecov/c/github/harens/checkdigit?logo=codecov&style=flat-square
   :alt: Codecov
   :target: https://app.codecov.io/gh/harens/checkdigit

.. image:: https://img.shields.io/pypi/dm/checkdigit?logo=python&logoColor=white&style=flat-square
   :alt: PyPi - Downloads
   :target: https://pepy.tech/project/checkdigit

.. image:: https://img.shields.io/codefactor/grade/github/harens/checkdigit?logo=codefactor&style=flat-square
   :alt: CodeFactor Grade
   :target: https://www.codefactor.io/repository/github/harens/checkdigit/

.. image:: https://img.shields.io/lgtm/grade/python/github/harens/checkdigit?logo=lgtm&style=flat-square
   :alt: LGTM Grade
   :target: https://lgtm.com/projects/g/harens/checkdigit/

=========

.. image:: https://repology.org/badge/vertical-allrepos/python:checkdigit.svg
   :alt: checkdigit repology
   :target: https://repology.org/project/python:checkdigit/versions
   :align: right

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

* `Even/Odd binary parity <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.parity.html#module-checkdigit.parity>`_
* `CRC <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.crc.html#module-checkdigit.crc>`_
  (credit to `@sapieninja <https://github.com/sapieninja>`_)
* `GS1 Standards <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.gs1.html#module-checkdigit.gs1>`_ (credit to `@OtherBarry <https://github.com/OtherBarry>`_)
    * EAN-8/13
    * GDTI
    * GLN
    * SSCC
    * UPC-A/E
    * etc. *(all fixed length numeric GS1 data structures with a check digit)*
* `ISBN-10/13 <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.isbn.html#module-checkdigit.isbn>`_
* `Luhn <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.luhn.html#module-checkdigit.luhn>`_
* `Verhoeff <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.verhoeff.html#module-checkdigit.verhoeff>`_

For each of these formats, we provide functions to validate them and calculate missing digits.

Do you have any formats that you'd like to see supported? 🤔 Feel free to raise an issue,
or even to send a pull request!

🔨 Contributing
---------------

- Contributing Page: `<https://checkdigit.rtfd.io/en/latest/contributing.html>`_
- Issue Tracker: `<https://github.com/harens/checkdigit/issues>`_
- Source Code: `<https://github.com/harens/checkdigit>`_

Any change, big or small, that you think can help improve this project is more than welcome 🎉.

As well as this, feel free to open an issue with any new suggestions or bug reports. Every contribution is appreciated.

To find out more, please read our `contributing page <https://checkdigit.readthedocs.io/en/latest/contributing.html>`_. Thank you!

📙 License
-----------

This project is licensed under `GPL-3.0-or-later <https://github.com/harens/checkdigit/blob/master/LICENSE>`_.
