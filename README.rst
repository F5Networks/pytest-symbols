pytest-symbols
==============

|Build Status|

Overview
--------

-  pytest-symbols is a pytest plugin that adds support for passing test
   environment symbols into pytest tests.
-  The supported formats for symbols files are json and yaml.

Installation
------------

.. code:: shell

    pip install https://github.com/F5Networks/pytest-symbols.git

Usage
-----

-  use the "--symbols" option to pass symbols into a pytest run:

.. code:: shell

    py.test --symbols tests/demo.json -- tests/demo.py

-  use the "symbols" fixture to access symbols within a test:

.. code:: python

    def test_with_symbols_fixture(self, symbols):
        print symbols
        assert symbols.client_ip == "192.168.1.1"
        assert symbols.server_ip == "192.168.2.1"

-  use "pytest.symbols" to access symbols outside the "symbols" fixture:

.. code:: python

    import pytest

    from pytest import symbols as foo


    def test_without_symbols_fixture(self):
        print pytest.symbols
        assert symbols.client_ip == "192.168.1.1"
        assert symbols.server_ip == "192.168.2.1"    
        print foo
        assert foo.client_ip == "192.168.1.1"
        assert foo.server_ip == "192.168.2.1"

Documentation
-------------

https://pytest-symbols.readthedocs.org

How to Contribute
-----------------

-  Contributions are warmly welcomed.
-  Contributions should be associated with an open issue.
-  Find an open issue that interests you, or create a new one if you
   don't find what you're looking for in the backlog.
-  Fork this repository on GitHub and make your changes in the master
   branch (or branch off of it).
-  Write tests that verify the issue has been resolved (ie. the bug was
   fixed or the new feature works as expected).
-  Add yourself to AUTHORS.rst.
-  Send a pull request.
-  Sit back and wait for the plaudits to roll in.

Contact
-------

qetools@f5.com

Support
-------

See `Support <SUPPORT.rst>`__

Copyright
---------

Copyright 2016 F5 Networks Inc.

Contributor License Agreement
-----------------------------

Individuals or business entities who contribute to this project must
have completed and submitted the `F5 Contributor License
Agreement <http://f5-openstack-docs.readthedocs.org/en/latest/cla_landing.html>`__
to Openstack\_CLA@f5.com prior to their code submission being included
in this project.

License
-------

Apache V2.0
^^^^^^^^^^^

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. |Build Status| image:: https://travis-ci.org/F5Networks/pytest-symbols.svg?branch=master
   :target: https://travis-ci.org/F5Networks/pytest-symbols
