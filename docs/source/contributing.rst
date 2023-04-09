Contributing
*************

- Issue Tracker: `<https://github.com/harens/checkdigit/issues>`_
- Source Code: `<https://github.com/harens/checkdigit>`_

Any change, big or small, that you think can help improve this project is more than welcome 🎉.

As well as this, feel free to open an issue with any new suggestions or bug reports. Every contribution is appreciated.

Contributors ✨
----------------

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
        <td align="center" valign="top" width="14.28%"><a href="http://mohsen.1.banan.byname.net/contact"><img src="https://avatars.githubusercontent.com/u/39976397?v=4?s=100" width="100px;" alt="Mohsen BANAN"/><br /><sub><b>Mohsen BANAN</b></sub></a><br /><a href="https://github.com/harens/checkdigit/issues?q=author%3AmohsenBanan" title="Bug reports">🐛</a></td>
      </tr>
    </table>

    <!-- markdownlint-restore -->
    <!-- prettier-ignore-end -->

    <!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the `all-contributors <https://github.com/all-contributors/all-contributors>`_ specification. Contributions of any kind welcome!

🏗 Setup
---------

First, fork the `GitHub project <https://github.com/harens/checkdigit>`_ to your account. Then, run the following with your GitHub handle in place of
:code:`INSERT_GITHUB_NAME`:

.. code-block:: console

    git clone https://github.com/INSERT_GITHUB_NAME/checkdigit
    cd checkdigit
    poetry install && poetry shell
    pre-commit install

Before submitting any new changes, please run :code:`make` beforehand. This formats the code and runs the tests. Thank you :)

🏛 Project structure
---------------------

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

Each new format should go into a separate file which is named accordingly.

📚 Building the Docs
---------------------

The documentation can be found in :code:`docs/source`.

We can use `sphinx-autobuild <https://github.com/executablebooks/sphinx-autobuild>`_ to continuously rebuild the docs when changes are made.

.. code-block:: console

    make docs

🎪 File structure
------------------

Similar data formats should use the same function (e.g. ISBN-10 and ISBN-13 functions determine the length before calculations).

Each of the Python files follow the same general format:

.. code-block:: python

    # License + File docstring

    from checkdigit._data import cleanse, convert, missing_template


    def calculate(data: str) -> str:
        """Determines check digit.

        Args:
            data: A string of data missing a check digit

        Returns:
            str: The single missing check digit (not the whole block of data)

        Examples:
            >>> # These should show some different applications of the function.
            >>> from checkdigit import ...
            >>> calculate(...)
            "output"
        """
        # This helps to deal with user formatting inconsistencies
        # e.g. spaces, hyphens, etc.
        data = cleanse(data)

        # Insert logic here

        # convert() deals with 10 or 11 being the possible check digit
        # N.B. This might not always be necessary if 10/11 aren't options (e.g. binary parity)
        return convert(...)


    def validate(data: str) -> bool:
        """Validates a block of data from the check digit.

        Args:
            data: A string representing a full block of data

        Returns:
            bool: A boolean representing whether the data is valid or not

        Examples:
            >>> # These should show some different applications of the function.
            >>> from checkdigit import ...
            >>> validate(...)
            "output"
        """

        # Remove the check digit and see if it matches
        # calculate() cleanses the data for us
        return calculate(data[:-1]) == data[-1]


    def missing(data: str) -> str:
        """Returns the missing digit from a block of data.

        Args:
            data: A string with a question mark in the place of a missing digit.

        Returns:
            A string representing the missing digit (not the whole block of data)

        Examples:
            >>> # These should show some different applications of the function.
            >>> from checkdigit import ...
            >>> missing(...)
            "output"
        """

        # For the majority of formats, there's a default template that should work well
        # This just brute forces the digits from 0-9 and runs validate() on it.
        return missing_template(data, "module-name")
