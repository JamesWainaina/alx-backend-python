#!/usr/bin/env python3

"""
Parametizing a unit test using utils.access_nested_map function
"""

import unittest
from typing import Any, Mapping, Sequence
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected_error: Any) -> Any:
        """
        Test method for error exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping) -> Any:
        """
        Test method for get_json function
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch("requests.get", return_value=mock_response):
            self.assertEqual(get_json(test_url), test_payload)
