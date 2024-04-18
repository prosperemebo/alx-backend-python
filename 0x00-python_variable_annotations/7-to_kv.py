#!/usr/bin/env python3
""" Type-annotated function to_kv """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-annotated implementation for to_kv"""
    return (k, v ** 2)
