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


"""
pytest_symbols.exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~
This module defines the exceptions used in pytest_symbols.

"""


class SymbolsError(Exception):
    """Base class for pytest_symbols exceptions."""

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        classname = self.__class__.__name__
        if self.msg:
            return self.msg
        else:
            return classname


class SymbolsFileNotFoundError(SymbolsError):
    """Failed to find the specified symbols file."""


class SymbolsFileFormatError(SymbolsError):
    """Symbols file has invalid file extension."""
