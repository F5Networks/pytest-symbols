pytest-symbols
==============


Overview
--------
- pytest-symbols is a pytest plugin that adds support for passing
  test environment symbols into pytest tests.
- The supported formats for symbols files are json and yaml.


Installation
------------
```shell
  $ pip install pytest-symbols
```


Usage
-----
- use the "--symbols" option to pass symbols into a pytest run:

```shell
  $ py.test --symbols tests/demo.json -- tests/demo.py
```


- pass the "symbols" fixture to access symbols within a test:

```python
  def test_symbols(self, symbols):
      print symbols
      assert symbols.client_ip == "1.1.1.1"
      assert symbols.server_ip == "2.2.2.2"
```


Documentation
-------------
https://pytest-symbols.readthedocs.org


How to Contribute
-----------------
- Contributions are warmly welcomed.
- Contributions should be associated with an open issue.
- Find an open issue that interests you, or create a new one if you don't find
  what you're looking for in the backlog.
- Fork this repository on GitHub and make your changes in the master branch
  (or branch off of it).
- Write tests that verify the issue has been resolved (ie. the bug was fixed
  or the new feature works as expected).
- Add yourself to AUTHORS.rst.
- Send a pull request.
- Sit back and wait for the plaudits to roll in.


Contact
-------
qetools@f5.com


Copyright
---------
Copyright 2016 F5 Networks Inc.


License
-------

#### Apache V2.0
Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations
under the License.
