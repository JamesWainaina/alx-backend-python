#!/usr/bin/python3

"""
Parametizing a unit test using utils.access_nested_map function
"""

import unittest
from typing import Any, Mapping, Sequence
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2},),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_path: Sequence) -> Any:
        """
        Test method for access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_path)
