==============================================================================
A robot framework library for JWT authentication.
==============================================================================

.. image:: https://travis-ci.org/kitconcept/robotframework-jwt.svg?branch=master
    :target: https://travis-ci.org/kitconcept/robotframework-jwt

.. image:: https://img.shields.io/pypi/status/robotframework-jwt.svg
    :target: https://pypi.python.org/pypi/robotframework-jwt/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/v/robotframework-jwt.svg
    :target: https://pypi.python.org/pypi/robotframework-jwt/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/robotframework-jwt.svg
    :target: https://pypi.python.org/pypi/robotframework-jwt/
    :alt: License

|

.. image:: https://raw.githubusercontent.com/kitconcept/robotframework-jwt/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/


Introduction
------------

robotframework-jwt is a web testing library to test Django with Robot Framework. It uses Selenium2Library to run tests against a real browser instance.

The library will automatically start and stop your Django instance while running the tests. It also comes with serveral autologin keywords that allow you to login different users during your tests, without the need to actually access the login page.

jwt is tested against Django 1.8.x and 1.9.x with SQLite and Postgres on Python 2.7 and 3.5.


Documentation
-------------

`Robot Framework JWT Library Keyword Documentation`_


Installation
------------

Install robotframework-jwt with pip::

  $ pip install robotframework-jwt

License
-------

Copyright kitconcept GmbH.

Distributed under the terms of the Apache License 2.0, robotframework-jwt is free and Open Source software.


Contribute
----------

- `Source code at Github <https://github.com/kitconcept/robotframework-jwt>`_
- `Issue tracker at Github <https://github.com/kitconcept/robotframework-jwt/issues>`_


Support
-------

If you are having issues, `please let us know <https://github.com/kitconcept/robotframework-jwt/issues>`_. If you require professional support feel free to contact us at `info@kitconcept.com. <mailto:info@kitconcept.com>`_


Development
-----------

Checkout repository from github::

  $ git clone https://github.com/kitconcept/robotframework-jwt.git

Create a virtual Python environment::

  $ cd robotframework-jwt/
  $ virtualenv .py27
  $ source .py27/bin/activate

Install robotframework-jwt in development mode::

  $ python setup.py develop

Install the requirements::

  $ pip install -r requirements.txt

Run Unit/Integration-Tests::

  $ py.test tests/

.. _`Robot Framework Django Library Keyword Documentation`: https://kitconcept.github.io/robotframework-jwt/
