.. raw:: html

    <p align="center">
        <a href="#readme">
            <img alt="checkdigit logo" src="https://raw.githubusercontent.com/harens/checkdigit/master/art/logo.png">
            <!-- README inspired by loguru -->
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/harens/checkdigit/actions">
            <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/harens/checkdigit/test.yml?logo=github&style=flat-square">
        </a>
        <a href="https://app.codecov.io/gh/harens/checkdigit">
            <img alt="Codecov" src="https://img.shields.io/codecov/c/github/harens/checkdigit?logo=codecov&style=flat-square">
        </a>
        <a href="https://pepy.tech/project/checkdigit">
            <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/checkdigit?logo=python&logoColor=white&style=flat-square">
        </a>
        <a href="https://www.codefactor.io/repository/github/harens/checkdigit/">
            <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/harens/checkdigit?logo=codefactor&style=flat-square">
        </a>
    </p>
    <p align="center">
        <a href="#readme">
            <img alt="checkdigit example" src="https://raw.githubusercontent.com/harens/checkdigit/master/art/demo.gif">
        </a>
    </p>

=========

.. raw:: html

    <a href="https://repology.org/project/python:checkdigit/versions">
        <img src="https://repology.org/badge/vertical-allrepos/python:checkdigit.svg" alt="Packaging status" align="right">
    </a>

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

* 📦 Works out of the box with all `supported Python versions <https://endoflife.date/python>`_ (3.7-3.11).
* ⌨️ `PEP 561 compatible <https://www.python.org/dev/peps/pep-0561>`_, with built in support for type checking.
* 🏃 Zero runtime dependencies. What you see is what you get.
* 🧮 Capable of calculating missing digits or validating a block of data.
* 📝 Extensive in-code comments and docstrings to explain how it works behind the scenes.

✅ Supported Formats
---------------------

* `Even/Odd binary parity <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.parity.html#module-checkdigit.parity>`_
* `CRC <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.crc.html#module-checkdigit.crc>`_
* `GS1 Standards <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.gs1.html#module-checkdigit.gs1>`_
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

✨ Contributors
----------------

This project follows the `all-contributors <https://github.com/all-contributors/all-contributors>`_ specification. Contributions of any kind are welcome!

Want to help out? Check out the `contributing page <https://checkdigit.rtfd.io/en/latest/contributing.html>`_.

Thanks goes to these wonderful people (`emoji key <https://allcontributors.org/docs/en/emoji-key>`_):

.. raw:: html

    <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
    <!-- prettier-ignore-start -->
    <!-- markdownlint-disable -->
    <table>
      <tr>
        <td align="center"><a href="https://zeevox.net"><img src="https://avatars.githubusercontent.com/u/8385172?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Timothy Langer</b></sub></a><br /><a href="https://github.com/harens/checkdigit/commits?author=ZeevoX" title="Tests">⚠️</a> <a href="https://github.com/harens/checkdigit/commits?author=ZeevoX" title="Documentation">📖</a></td>
        <td align="center"><a href="https://github.com/OtherBarry"><img src="https://avatars.githubusercontent.com/u/6956537?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Charlie Wilson</b></sub></a><br /><a href="https://github.com/harens/checkdigit/commits?author=OtherBarry" title="Code">💻</a> <a href="https://github.com/harens/checkdigit/commits?author=OtherBarry" title="Tests">⚠️</a></td>
        <td align="center"><a href="https://github.com/sapieninja"><img src="https://avatars.githubusercontent.com/u/60101890?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Max Bowman</b></sub></a><br /><a href="https://github.com/harens/checkdigit/commits?author=sapieninja" title="Code">💻</a> <a href="https://github.com/harens/checkdigit/commits?author=sapieninja" title="Tests">⚠️</a></td>
        <td align="center"><a href="http://mohsen.1.banan.byname.net/contact"><img src="https://avatars.githubusercontent.com/u/39976397?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mohsen BANAN</b></sub></a><br /><a href="https://github.com/harens/checkdigit/issues?q=author%3AmohsenBanan" title="Bug reports">🐛</a></td>
      </tr>
    </table>

    <!-- markdownlint-restore -->
    <!-- prettier-ignore-end -->

    <!-- ALL-CONTRIBUTORS-LIST:END -->

📙 License
-----------

This project is licensed under `GPL-3.0-or-later <https://github.com/harens/checkdigit/blob/master/LICENSE>`_.
