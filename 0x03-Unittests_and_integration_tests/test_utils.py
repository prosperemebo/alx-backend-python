#!/usr/bin/env python3
""" this module contains TestAccessNestedMap implementations """

from typing import Mapping, Sequence, Any, Dict
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
from parameterized import parameterized
from unittest import TestCase


class TestAccessNestedMap(TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self,
        n_map: Mapping,
        path: Sequence,
        expected: Any,
    ):
        """Test successful access_nested_map."""
        self.assertEqual(access_nested_map(n_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(
        self,
        n_map: Mapping,
        path: Sequence,
    ):
        """Test expected exceptions during access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(n_map, path)


class TestGetJson(TestCase):
    """Implementation of TestGetJson"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url: str, test_payload: Dict):
        """Test the get_json function by mocking the requests.get method."""
        mocked_response = Mock()
        mocked_response.json.return_value = test_payload

        with patch("requests.get", return_value=mocked_response) as mocked_get:
            output = get_json(url)

        mocked_get.assert_called_once_with(url)
        self.assertEqual(output, test_payload)
