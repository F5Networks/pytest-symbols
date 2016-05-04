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


"""This module defines the pytest-symbols plugin object model."""


import copy
import os
import yaml

from . import exceptions


class Symbols(object):
    """Base class for the pytest-symbols plugin."""

    def __init__(self, symbols_file=""):
        """Construct the symbols object.

        :param str symbols_file: path to the symbols file we want to load
        :return: None
        """
        self._symbols_file = symbols_file
        self.load_symbols()

    def __str__(self):
        """String representation of the symbols object (public members only).

        :return: str
        """
        members = copy.deepcopy(self.__dict__)
        for k in members.keys():
            if k.startswith("_"):
                members.pop(k)
        return str(members)

    def load_symbols(self):
        """Load symbols from the symbols file.

        :return: None
        """
        if not self._symbols_file:
            return
        symbols = self._load_symbols_file(self._symbols_file)
        self.__dict__.update(symbols)

    def _load_symbols_file(self, filepath):
        filepath = os.path.abspath(os.path.expanduser(filepath))
        if not os.path.exists(filepath):
            raise exceptions.SymbolsFileNotFoundError(
                "Symbols file not found ('%s')." % filepath
            )
        with open(filepath, 'r') as f:
            data = yaml.load(f)
        return data
