#!/usr/bin/env python3

"""
Module to test out the calculator
"""

from .. import calculator
from unittest import TestCase


class TestCaculator(TestCase):
    """
    testing the functions
    """

    def test_function_docs(self):
        """
        Make sure the functions are well documented
        """
        self.assertIsNotNone(calculator.add.__doc__)
        self.asertIsNotNone(calculator.multiply.__doc__)

    def test_add_function(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_multiply_function(self):
        self.assertEqual(calculator.multiply(1, 3), 3)
