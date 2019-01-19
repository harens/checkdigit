# /usr/bin/env python

# This file is part of checkdigit.

# Types-and-Variables is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# checkdigit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with checkdigit.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="checkdigit",
    version="0.0.2",
    description="Checking digits with a digit!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="harens",
    license="GPLv3",
    packages=find_packages(exclude=("tests",)),
    author_email="harensdeveloper@gmail.com",
    url="https://harens.github.io",
    download_url="https://github.com/harens/checkdigit/tarball/0.0.1",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    project_urls={
        "Source": "https://github.com/harens/checkdigit",
        "Tracker": "https://github.com/harens/checkdigit/issues",
    },
    keywords="Check Digits, Validation, ISBN",
)
