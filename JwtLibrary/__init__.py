# -*- coding: utf-8 -*-
from robot.libraries.BuiltIn import BuiltIn

import requests
from robot.api import logger

import base64
import os
import six
import signal
import subprocess
import time

__version__ = '1.0'
ROBOT_LIBRARY_DOC_FORMAT = 'reST'


def safe_bytes(str):
    """Returns bytes on Py3 and a string on Py2."""
    if six.PY3:
        return bytes(str, 'utf-8')
    else:
        return str


def safe_utf8(string):
    """Returns bytes on Py3 and an utf-8 encoded string on Py2."""
    if six.PY2:
        return string.encode("utf-8")
    else:
        return string


class JwtLibrary:
    """Minimal example for a Robot Framework Library.
    """

    # TEST CASE => New instance is created for every test case.
    # TEST SUITE => New instance is created for every test suite.
    # GLOBAL => Only one instance is created during the whole test execution.
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        """WebpackLibrary can be imported with optional arguments.
        """
        pass

    def enable_jwt_autologin_as(self, *args, **kwargs):

        # XXX: HOST/POST/PATH are currently hard-coded!!!
        response = requests.post(
            'http://localhost:55001/plone/@login',
            headers={'Accept': 'application/json'},
            json={'login': 'admin', 'password': 'secret'}
        )
        token = response.json().get('token')

        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        # seleniumlib.go_to('http://localhost:4300')
        # autologin_cookie_value = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmdWxsbmFtZSI6bnVsbCwic3ViIjoiYWRtaW4iLCJleHAiOjE1MzIzMjYzMzN9.ezy8qv5eEy1-kk8XxnaZqFKj1_1-V75Pi6FlvgnkwQA'
        seleniumlib.execute_javascript(
            "document.cookie = 'auth_token=%s;path=/;domain=localhost;';" %
            token
        )

        # XXX: use local storage for cookie persistence?
        # seleniumlib.execute_javascript(
        #     "localStorage.setItem('token', '{}')".format(token)
        # )

        # XXX: does not work without a short sleep
        time.sleep(2)

        if seleniumlib.get_cookies().startswith('auth_token'):
            return token

        # seleniumlib.go_to('http://localhost:4300')
        # browser = seleniumlib._current_browser()
        # import sys
        # import pdb
        # pdb.Pdb(stdout=sys.__stdout__).set_trace()
        # seleniumlib.wait_until_page_contains('Plone')
        # seleniumlib.wait_until_page_contains_element('css=.left.fixed.menu')
        return token
