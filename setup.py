#!/usr/bin/env python


# Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""This module makes the pytest-symbols plugin pip installable."""


from setuptools import setup, find_packages

import pytest_symbols


def read(f):
    """Read contents of specified file."""
    return open(f).read().strip()


setup(
    name="pytest_symbols",
    version=pytest_symbols.VERSION,
    description=(
        "pytest-symbols is a pytest plugin that adds support for passing "
        "test environment symbols into pytest tests."
    ),
    long_description=read("README.rst"),
    author="F5 Networks",
    author_email="qetools@f5.com",
    url="https://github.com/F5Networks/pytest-symbols",
    keywords=["F5", "testing"],
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=["PyYAML>5"],
    entry_points={
        'pytest11': ["symbols = pytest_symbols.plugin"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing"
    ]
)
