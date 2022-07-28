"""
An example of a basic unit test, and test cases
that use the `unittest.TestCase` class.
"""

from unittest import TestCase

import package_name


def test_package_name_instantiates():
    # A smoke test
    obj = package_name.SampleObject()
    assert obj


class SampleObjectTestCase(TestCase):
    def setUp(self):
        # this is always ran before each test on this object
        self.Iobj = package_name.SampleObject()

    def tearDown(self):
        # this is always ran after each test on this object
        pass

    def test_fizz(self):
        assert self.Iobj.fizz() == "buzz"
