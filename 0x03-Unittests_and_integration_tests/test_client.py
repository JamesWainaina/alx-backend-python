#!/usr/bin/env python3

"""
Using Parameterize and patch as decorators
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, MagicMock, Mock
from requests import HTTPError
from typing import Any, Dict
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient class
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    async def test_org(self, org_name: str, mock_get_json: Any) -> None:
        """
        Test org method
        """
        mock_get_json.return_value = {"name": org_name}

        client: GithubOrgClient = GithubOrgClient(org_name)
        result: Dict[str, Any] = await client.org()

        self.assertEqual(result, {"name": org_name})
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
