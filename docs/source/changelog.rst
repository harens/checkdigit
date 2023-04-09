Changelog
**********

0.5.0 (2023-04-09)
===================

🐛 Bugfixes
------------

- Fixed a bug where ISBN-13 calculations allowed for a check digit of X, which shouldn't be possible. (`#171 <https://github.com/harens/checkdigit/issues/171>`_)

0.4.0 (2023-01-15)
===================

🔨 Compatibility Broken
-------------------------

- Dropped support for Python 3.6

⚡️ Features
------------

- Added support for Python 3.10 and 3.11

0.3.1 (2021-07-27)
===================

⚡️ Features
------------

- Added support for the Verhoeff algorithm.

🎭 Behind the Scenes
---------------------

- The :code:`missing` method has been refactored into one central location to massively reduce code duplication.
- The numerous shell scripts for formatting/testing were replaced with a single Makefile.

0.3.0 (2021-06-21)
===================

🔨 Compatibility Broken
-------------------------

- A single ISBN function is now available, rather than the two separate ones for ISBN-10 and ISBN-13.
  (`#19 <https://github.com/harens/checkdigit/issues/19>`_ `#63 <https://github.com/harens/checkdigit/issues/63>`_)

⚡️ Features
------------

- Improved support for GS1-based codes, such as EAN-8 and UPC-E. (`#19 <https://github.com/harens/checkdigit/issues/19>`_)

📚 Improved Documentation
---------------------------

- Added changelog and contributing pages.
- On the main README, the individual GS1 and GTIN formats that are supported are noted (e.g. ISBN-10, GDTI, etc.)

🎭 Behind the Scenes
---------------------

- The build tests were separated from the linting tests. (`#66 <https://github.com/harens/checkdigit/issues/66>`_)

0.2.0 (2021-05-21)
===================

⚡️ Features
------------

- CRC Format Added (Thanks `@sapieninja! <https://github.com/sapieninja>`_). (`#42 <https://github.com/harens/checkdigit/pull/42>`_)

📚 Improved Documentation
---------------------------

- The `Python API <https://checkdigit.readthedocs.io/en/stable/reference.html>`_ has been documented with examples.
- Revamped the `README <https://github.com/harens/checkdigit/blob/master/README.rst>`_.
- Add a `contributors section <https://github.com/harens/checkdigit/tree/v0.2.0#contributors->`_ to appreciate everyone's help!

🎭 Behind the Scenes
---------------------

- Transition tests from `error404 <https://github.com/harens/error404>`_ to `pytest <https://pytest.org/>`_.
- Move from GitHub Wiki to RTD (where you're currently reading this). (`#41 <https://github.com/harens/checkdigit/issues/41>`_)
- Refactored ISBN and Luhn code.

0.1.2 (2021-05-04)
===================

⚡️ Features
------------

- GS1 Format Added (Thanks `@OtherBarry! <https://github.com/OtherBarry>`_). (`#38 <https://github.com/harens/checkdigit/pull/38>`_)

0.1.1 (2020-12-04)
===================

⚡️ Features
------------

- `PEP 561 compatible <https://www.python.org/dev/peps/pep-0561/>`_, with support for type checking.

📚 Improved Documentation
---------------------------

- Updated docstrings and inline documentation.

🎭 Behind the Scenes
---------------------

- Test script written to check formatting and improve code consistency.
