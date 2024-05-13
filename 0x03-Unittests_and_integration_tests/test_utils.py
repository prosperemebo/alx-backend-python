#!/usr/bin/env python3
""" this module contains TestAccessNestedMap implementations """

from typing import Mapping, Sequence, Any
from parameterized import parameterized
from utils import access_nested_map
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
