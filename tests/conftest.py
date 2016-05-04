"""Sample local pytest plugin (aka conftest file)."""


import pytest

from pytest import symbols as symbols_data


@pytest.fixture()
def fx_foo(request):
    """Fixture that accesses symbols data from within a conftest file."""
    print "hello from fx_foo ..."
    print symbols_data
