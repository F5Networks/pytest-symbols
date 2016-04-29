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


"""This module contains tests for the pytest-symbols plugin."""


import pytest

pytest_plugins = "pytester,symbols"


_SYMBOLS_PATTERN_JSON = """
    {{
        "client_ip{0}": "1.1.1.1",
        "server_ip{0}": "2.2.2.2"
    }}
"""
_SYMBOLS_PATTERN_YAML = """
    client_ip{0}: 1.1.1.1
    server_ip{0}: 2.2.2.2
"""


def test_no_cli_arg(testdir):
    """Test that a failure occurs if no argument is passed to --symbols.

    Args:
        testdir: The pytest plugin testing utility.
    """
    testdir.makepyfile("""
        pytest_plugins = "pytester,symbols"

        def test(testdir):
            testdir.makepyfile(\"\"\"
                def test_internal():
                    pass
            \"\"\")
            result = testdir.runpytest('--symbols')
            result.assert_outcomes(failed=1)
    """)
    result = testdir.runpytest()
    assert 'argument --symbols: expected one argument' in result.stdout.str()


def test_no_symbols(testdir):
    """Test that no symbols object is created if no ini or arg are specified.

    Args:
        testdir: The pytest plugin testing utility.
    """
    testdir.makepyfile("""
        def test(symbols):
            assert not symbols
    """)
    result = testdir.runpytest()
    result.assert_outcomes(passed=1)


@pytest.mark.parametrize('ext, data', [
    ('.json', _SYMBOLS_PATTERN_JSON.format('')),
    ('.yaml', _SYMBOLS_PATTERN_YAML.format(''))
])
def test_cli(testdir, ext, data):
    """Test that a symbols file specified on the command line loads symbols.

    Args:
        testdir: The pytest plugin testing utility.
        ext: The file extension for the symbols file.
        data: The file contents for the symbols file.
    """
    data_file = testdir.makefile(ext, data)
    testdir.makepyfile("""
        def test(symbols):
            assert symbols
            assert symbols.client_ip == '1.1.1.1'
            assert symbols.server_ip == '2.2.2.2'
    """)
    result = testdir.runpytest('--symbols', data_file)
    result.assert_outcomes(passed=1)


@pytest.mark.parametrize('ext, data', [
    ('.json', """
        {
            "outer":
            {
                "client_ip": "1.1.1.1",
                "server_ip": "2.2.2.2",
                "inner": {
                    "client_ip": "3.3.3.3"
                }
            }
        }
    """),
    ('.yaml', """
        outer:
            client_ip: 1.1.1.1
            server_ip: 2.2.2.2
            inner:
                client_ip: 3.3.3.3
    """)
])
def test_nested(testdir, ext, data):
    """Test that a symbols file specified on the command line loads symbols.

    Args:
        testdir: The pytest plugin testing utility.
        ext: The file extension for the symbols file.
        data: The file contents for the symbols file.
    """
    data_file = testdir.makefile(ext, data)
    testdir.makepyfile("""
        def test(symbols):
            assert symbols
            assert symbols.outer
            assert symbols.outer['client_ip'] == '1.1.1.1'
            assert symbols.outer['server_ip'] == '2.2.2.2'
            assert symbols.outer['inner']['client_ip'] == '3.3.3.3'
    """)
    result = testdir.runpytest('--symbols', data_file)
    result.assert_outcomes(passed=1)
