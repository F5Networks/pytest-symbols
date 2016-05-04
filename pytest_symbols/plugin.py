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


"""This module implements pytest hooks used by the pytest-symbols plugin."""


import pytest

from . import models


def pytest_addoption(parser):
    """Add command line options for the pytest-symbols plugin."""
    group = parser.getgroup("general")
    group.addoption(
        "--symbols",
        action="store",
        metavar="path",
        help="path for test environment symbols file"
    )


def pytest_load_initial_conftests(early_config, parser, args):
    """Add a private '_symbols' member to the standard 'config' object."""
    options = parser.parse_known_args(args)
    if options.symbols:
        early_config._symbols = models.Symbols(options.symbols)
        pytest.symbols = early_config._symbols


def pytest_namespace():
    """Add a 'symbols' object to the pytest namespace."""
    return {'symbols': None}


@pytest.fixture(scope="session", autouse=True)
def symbols(request):
    """Session-level fixture that returns the 'symbols' object."""
    symbols = getattr(request.config, "_symbols", None)
    return symbols
